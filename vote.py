# _*_ coding: utf-8 _*_
# by:Snowkingliu
# 2018/1/24 下午8:28

from flask import Flask, jsonify, json, g, request
from OpenSSL import SSL
import time
import hashlib

app = Flask(__name__)
vote_info = []
user_info = {}

# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('/root/snowkingliu.com/Nginx/2_snowkingliu.com.key')
# context.use_certificate_file('/root/snowkingliu.com/Nginx/1_snowkingliu.com_bundle.crt')

# context = ('/Users/xuejun/snowkingliu.com/Nginx/1_snowkingliu.com_bundle.crt',
#            '/Users/xuejun/snowkingliu.com/Nginx/2_snowkingliu.com.key')

context = ('/root/snowkingliu.com/Nginx/1_snowkingliu.com_bundle.crt',
           '/root/snowkingliu.com/Nginx/2_snowkingliu.com.key')

# context.use_privatekey_file('/Users/xuejun/snowkingliu.com/Nginx/2_snowkingliu.com.key')
# context.use_certificate_file('/Users/xuejun/snowkingliu.com/Nginx/1_snowkingliu.com_bundle.crt')


@app.before_request
def before_request():
    if not vote_info:
        load_file_data()


# # 已废弃
# @app.route('/vote/api/get_today_list')
# def get_today_list():
#     # 查找当前有效的订单
#     last_vote = vote_info[len(vote_info) - 1]
#     if last_vote["deadline"] > time.time() * 1000:
#         return jsonify({"vote_info": last_vote, "user_info": user_info[str(last_vote["vote_id"])]})
#     else:
#         return jsonify({"vote_info": [], "user_info": {}})


@app.route('/vote/api/get_vote_list')
def get_vote_list():
    # 查找全部的订单
    res = []
    for a_vote in vote_info[::-1]:
        ts_now = int(time.time()*1000)
        # 判断是否有效
        deadline = a_vote['deadline']
        if ts_now < deadline:
            next_day_start = ((ts_now + 8 * 3600 * 1000)/1000/3600/24 + 1)*24*3600*1000 - (8 * 3600 * 1000)
            # 当日投票
            if deadline < next_day_start:
                time_array = time.localtime(int(deadline/1000))
                res_data = time.strftime("%H:%M", time_array)
                res.append({
                    "enable": True,
                    "vote_id": a_vote['vote_id'],
                    "initiator": a_vote['initiator'],
                    "deadline": res_data,
                })
            else:
                # 明年及以后截止的投票
                time_array = time.localtime(int(deadline/1000))
                res_data = time.strftime("%m月%d日 %H:%M", time_array)
                res.append({
                    "enable": True,
                    "vote_id": a_vote['vote_id'],
                    "initiator": a_vote['initiator'],
                    "deadline": res_data,
                })
        # 已截止
        else:
            res.append({
                "enable": False,
                "vote_id": a_vote['vote_id'],
                "initiator": a_vote['initiator'],
            })
    return jsonify(res)


@app.route('/vote/api/get_vote_info')
def get_vote_info():
    vote_id = request.values.get("vote_id")
    a_vote = [a_vote for a_vote in vote_info if str(a_vote["vote_id"]) == str(vote_id)][0]
    initiator = a_vote['initiator']
    deadline_ts = a_vote['deadline']
    items_json = a_vote['items']
    ts_now = int(time.time()*1000)

    # 若已过期
    if deadline_ts < ts_now:
        deadline = "已截止"
        enable = False
    else:
        # 超过1天
        enable = True
        if deadline_ts - ts_now > 1000*3600*24:
            deadline = ">1天"
        elif deadline_ts - ts_now < 60 * 1000:
            deadline = "<1分钟"
        else:
            hour = (deadline_ts - ts_now)/1000/60/60
            minute = (deadline_ts - ts_now)/1000/60 % 60
            deadline = "{0}:{1}".format(hour, minute)
    items = []
    for i in range(len(items_json)):
        total = len(user_info[vote_id])
        choice_num = 0
        # choice_user_info = []
        user_avatar_url = []
        for nickname, choice_info in user_info[vote_id].items():
            if str(choice_info['choice']) == str(i):
                choice_num += 1
                # choice_user_info.append([nickname, choice_info['avatar_url']])
                if len(user_avatar_url) <= 9:
                    user_avatar_url.append(choice_info['avatar_url'])

        if total == 0:
            present = 0
        else:
            present = float(choice_num)/total*100
        items.append({
            "number": choice_num,
            "item_id": i,
            "item_name": items_json[str(i)],
            "img_id": i % 5,
            "present": present,
            # "choice_user_info": choice_user_info,
            "user_avatar_url": user_avatar_url
        })

    res = {
        "vote_id": vote_id,
        "initiator": initiator,
        "deadline": deadline,
        "items": items,
        "enable": enable
    }
    return jsonify(res)


@app.route('/vote/api/send_my_vote')
def send_my_vote():
    vote_id = request.values.get("vote_id")
    item_id = request.values.get("item_id")
    nick_name = request.values.get("nick_name")
    avatar_url = request.values.get("avatar_url")
    if nick_name in user_info[vote_id]:
        return jsonify({"success": False})
    else:
        res = {
            "timestamp": int(time.time()*1000),
            "avatar_url": avatar_url,
            "choice": item_id,
        }
        user_info[vote_id][nick_name] = res
        fp = open("user_info.txt", mode="w")
        fp.writelines(json.dumps(user_info))
        fp.close()
    return jsonify({"success": True})


@app.route('/vote/api/selected')
def selected():
    nick_name = request.values.get('nick_name')
    vote_id = request.values.get('vote_id')
    if nick_name in user_info[vote_id]:
        return jsonify({"selected": True})
    else:
        return jsonify({"selected": False})


@app.route('/vote/api/start_order')
def start_order():
    order_list = [order for order in request.values['order_list'].split(',') if order != ""]
    timestamp = int(time.time()*1000)
    initiator = request.values['nick_name']
    md5_obj = hashlib.md5()
    md5_obj.update("{0}-{1}".format(timestamp, initiator.encode("utf8")))
    vote_id = md5_obj.hexdigest()
    deadline = timestamp + 30 * 60 * 1000
    items = {}
    for i in range(len(order_list)):
        items[str(i)] = order_list[i]
    vote_info.append({
        "timestamp": timestamp,
        "initiator": initiator,
        "vote_id": vote_id,
        "deadline": deadline,
        "items": items,
    })
    fp = open("vote_info.txt", mode="w")
    fp.writelines(json.dumps(vote_info))
    fp.close()
    fp = open("user_info.txt", mode="w")
    user_info[vote_id] = {}
    fp.writelines(json.dumps(user_info))
    fp.close()
    return jsonify({"success": True})


def load_file_data():
    global vote_info, user_info
    fp = open("vote_info.txt", mode="rb")
    vote_info = json.loads(fp.readlines()[0])
    fp.close()
    fp = open("user_info.txt", mode="rb")
    user_info = json.loads(fp.readlines()[0])
    fp.close()


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000, ssl_context=context)



