# _*_ coding: utf-8 _*_
# by:Snowkingliu
# 2018/2/1 下午3:56
import json

questions = [
    {"number": 1, "question": "小说《哈利•波特》系列中，哈利最后和谁在一起了？", "answers": [{"option": "A", "id": "0", "answer": "赫敏"}, {"option": "B", "id": "1", "answer": "金妮"}, {"option": "C", "id": "2", "answer": "卢娜"}, {"option": "D", "id": "3", "answer": "罗恩"}]},
    {"number": 2, "question": "被称为“千湖之国”的是哪个国家？", "answers": [{"option": "A", "id": "0", "answer": "芬兰"}, {"option": "B", "id": "1", "answer": "希腊"}, {"option": "C", "id": "2", "answer": "挪威"}, {"option": "D", "id": "3", "answer": "印度尼西亚"}]},
    {"number": 3, "question": "十二星座中，摩羯座之后是哪个星座？", "answers": [{"option": "A", "id": "0", "answer": "双鱼座"}, {"option": "B", "id": "1", "answer": "水瓶座"}, {"option": "C", "id": "2", "answer": "射手座"}, {"option": "D", "id": "3", "answer": "金牛座"}]},
    {"number": 4, "question": "老版三国演义的主题曲歌词“滚滚长江东逝水，浪花淘尽英雄。是非成败转头空，青山依旧在，几度夕阳红。”是谁写的词？", "answers": [{"option": "A", "id": "0", "answer": "罗贯中"}, {"option": "B", "id": "1", "answer": "施耐庵"}, {"option": "C", "id": "2", "answer": "杨慎"}, {"option": "D", "id": "3", "answer": "解缙"}]},
    {"number": 5, "question": "云熵身高最高的男生是谁？", "answers": [{"option": "A", "id": "0", "answer": "张涛"}, {"option": "B", "id": "1", "answer": "许超"}, {"option": "C", "id": "2", "answer": "秦卓"}, {"option": "D", "id": "3", "answer": "曾月天"}]},
    {"number": 6, "question": "在20以内的数字，有多少个质数？", "answers": [{"option": "A", "id": "0", "answer": "6个"}, {"option": "B", "id": "1", "answer": "7个"}, {"option": "C", "id": "2", "answer": "8个"}, {"option": "D", "id": "3", "answer": "9个"}]},
    {"number": 7, "question": "著名作家巴金原名是？", "answers": [{"option": "A", "id": "0", "answer": "舒庆春"}, {"option": "B", "id": "1", "answer": "金岳霖"}, {"option": "C", "id": "2", "answer": "李尧棠"}, {"option": "D", "id": "3", "answer": "沈德鸿"}]},
    {"number": 8, "question": "世界上最大、最深的海是什么海？", "answers": [{"option": "A", "id": "0", "answer": "阿拉伯海"}, {"option": "B", "id": "1", "answer": "加勒比海"}, {"option": "C", "id": "2", "answer": "珊瑚海"}, {"option": "D", "id": "3", "answer": "地中海"}]},
    {"number": 9, "question": "动漫《美少女战士》中，水冰月的猫叫什么？", "answers": [{"option": "A", "id": "0", "answer": "美琪"}, {"option": "B", "id": "1", "answer": "小黑"}, {"option": "C", "id": "2", "answer": "露娜"}, {"option": "D", "id": "3", "answer": "雅美"}]},
    {"number": 10, "question": "首个获得英超金球奖的足球运动员是？", "answers": [{"option": "A", "id": "0", "answer": "贝克汉姆"}, {"option": "B", "id": "1", "answer": "内马尔"}, {"option": "C", "id": "2", "answer": "C罗"}, {"option": "D", "id": "3", "answer": "梅西"}]},
    {"number": 11, "question": "下列哪个女明星没有和霍建华演过情侣？", "answers": [{"option": "A", "id": "0", "answer": "陈乔恩"}, {"option": "B", "id": "1", "answer": "唐嫣"}, {"option": "C", "id": "2", "answer": "叶璇"}, {"option": "D", "id": "3", "answer": "林依晨"}]},
    {"number": 12, "question": "游戏《仙剑奇侠传3》里，火力全开下，实力仅次于重楼的是？", "answers": [{"option": "A", "id": "0", "answer": "邪剑仙"}, {"option": "B", "id": "1", "answer": "景天"}, {"option": "C", "id": "2", "answer": "紫萱"}, {"option": "D", "id": "3", "answer": "清微道长"}]},
    {"number": 13, "question": "下列哪位不在“唐宋八大家”之中？", "answers": [{"option": "A", "id": "0", "answer": "韩愈"}, {"option": "B", "id": "1", "answer": "曾巩"}, {"option": "C", "id": "2", "answer": "王安石"}, {"option": "D", "id": "3", "answer": "范仲淹"}]},
    {"number": 14, "question": "我们能够在路上行走，依靠的是物理上的什么力？", "answers": [{"option": "A", "id": "0", "answer": "向心力"}, {"option": "B", "id": "1", "answer": "重力"}, {"option": "C", "id": "2", "answer": "摩擦力"}, {"option": "D", "id": "3", "answer": "回复力"}]},
    {"number": 15, "question": "游戏“英雄联盟”里被大家称为“大头”的是谁？", "answers": [{"option": "A", "id": "0", "answer": "加里奥"}, {"option": "B", "id": "1", "answer": "潘森"}, {"option": "C", "id": "2", "answer": "波比"}, {"option": "D", "id": "3", "answer": "黑默丁格"}]},
    {"number": 16, "question": "2018是狗年，生肖“狗”对应的时辰是什么？", "answers": [{"option": "A", "id": "0", "answer": "酉"}, {"option": "B", "id": "1", "answer": "戌"}, {"option": "C", "id": "2", "answer": "戊"}, {"option": "D", "id": "3", "answer": "亥"}]},
    {"number": 17, "question": "NBA中被网友称为“神龟”的是谁？", "answers": [{"option": "A", "id": "0", "answer": "克里斯•保罗"}, {"option": "B", "id": "1", "answer": "詹姆斯•哈登"}, {"option": "C", "id": "2", "answer": "斯蒂芬•库里"}, {"option": "D", "id": "3", "answer": "威斯•布鲁克"}]},
    {"number": 18, "question": "靠变法使得秦国逐渐强大的商鞅，辅佐的是秦国哪个皇帝？", "answers": [{"option": "A", "id": "0", "answer": "秦穆公"}, {"option": "B", "id": "1", "answer": "秦孝公"}, {"option": "C", "id": "2", "answer": "秦襄公"}, {"option": "D", "id": "3", "answer": "秦庄公"}]},
    {"number": 19, "question": "以下哪个不是西施的名字或者别称？", "answers": [{"option": "A", "id": "0", "answer": "夷光"}, {"option": "B", "id": "1", "answer": "丽姬"}, {"option": "C", "id": "2", "answer": "明妃"}, {"option": "D", "id": "3", "answer": "浣纱女"}]},
    {"number": 20, "question": "Java之父是谁？", "answers": [{"option": "A", "id": "0", "answer": "瑞特•巴特勒"}, {"option": "B", "id": "1", "answer": "詹姆斯•高斯林"}, {"option": "C", "id": "2", "answer": "丹尼斯•里奇"}, {"option": "D", "id": "3", "answer": "哈利•波特"}]},
]

fp = open("questions.txt", mode="w")
fp.writelines(json.dumps(questions))
fp.close()

model_answers = [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 3, 1, 3, 2, 3, 1]

fp = open("model_answers.txt", mode="w")
fp.writelines(json.dumps(model_answers))
fp.close()
