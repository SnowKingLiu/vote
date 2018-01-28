# _*_ coding: utf-8 _*_
# by:Snowkingliu
# 2018/1/25 上午9:53
import json

a = [
    # {"timestamp": 1516803459309, "initiator": "Mellon", "vote_id": 0, "deadline": 1516807335420, "items": {"0": u"吃羊", "1": u"吃牛肉"}},
    # {"timestamp": 1516803459309, "initiator": "Mellon", "vote_id": 1, "deadline": 1516807335420, "items": {"0": u"吃肉", "1": u"吃炸鸡"}},
    # {"timestamp": 1516803459309, "initiator": "Mellon", "vote_id": 2, "deadline": 1516807335420, "items": {"0": u"吃鱼", "1": u"吃火腿肠"}},
    # {"timestamp": 1516803459309, "initiator": "Mellon", "vote_id": 3, "deadline": 1539917335420, "items": {"0": u"吃鸡", "1": u"吃麻辣烫", "2": u"吃菠萝", "3": u"吃巧克力", "4": u"吃烤鸭", "5": u"吃火锅"}},
]
fp = open("vote_info.txt", mode="w")
fp.writelines(json.dumps(a))
fp.close()

b = {
    0: [{"timestamp":1516803459309, "user": "Mellon", "choice": 0}, {"timestamp":1516803459309, "user": "Amanda", "choice": 0}],
    1: [{"timestamp":1516803459309, "user": "Mellon", "choice": 0}, {"timestamp":1516803459309, "user": "Amanda", "choice": 0}],
    2: [{"timestamp": 1516803459309, "user": "Mellon", "choice": 0},{"timestamp": 1516803459309, "user": "Amanda", "choice": 0}],
    3: [{"timestamp":1516803459309, "user": "Mellon", "choice": 0}, {"timestamp":1516803459309, "user": "Amanda", "choice": 0}, {"timestamp":1516803449309, "user": "Tom", "choice": 0}]
}

nb = {
    # 0: {
    #     # "Mellon": {"timestamp":1516803459309, "avatar_url": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqY2Z0bpmlYeGNZKq4nB7MowHHiciba6H6aiarWbJkBtbjgcncOLIfXI2ve7fuga0Gfoib54hGb8hYib8A/0", "choice": 0}
    # },
    # 1: {
    #     "Mellon": {"timestamp":1516803459309, "avatar_url": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqY2Z0bpmlYeGNZKq4nB7MowHHiciba6H6aiarWbJkBtbjgcncOLIfXI2ve7fuga0Gfoib54hGb8hYib8A/0", "choice": 0}
    # },
    # 2: {
    #     "Mellon": {"timestamp":1516803459309, "avatar_url": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqY2Z0bpmlYeGNZKq4nB7MowHHiciba6H6aiarWbJkBtbjgcncOLIfXI2ve7fuga0Gfoib54hGb8hYib8A/0", "choice": 0}
    # },
    # 3: {
    #     # "Mellon": {"timestamp":1516803459309, "avatar_url": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqY2Z0bpmlYeGNZKq4nB7MowHHiciba6H6aiarWbJkBtbjgcncOLIfXI2ve7fuga0Gfoib54hGb8hYib8A/0", "choice": 0}
    # },
}

fp = open("user_info.txt", mode="w")
fp.writelines(json.dumps(nb))
fp.close()

