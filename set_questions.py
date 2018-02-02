# _*_ coding: utf-8 _*_
# by:Snowkingliu
# 2018/2/1 下午3:56
import json

questions = [
    {"number": 1, "question": "1+1=?", "answers": [{"option": "A", "id": "0", "answer": "2"}, {"option": "B", "id": "1", "answer": "3"}, {"option": "C", "id": "2", "answer": "7"}, {"option": "D", "id": "3", "answer": "9"}]},
    {"number": 2, "question": "2+5=?", "answers": [{"option": "A", "id": "0", "answer": "2"}, {"option": "B", "id": "1", "answer": "3"}, {"option": "C", "id": "2", "answer": "7"}, {"option": "D", "id": "3", "answer": "9"}]},
]

fp = open("questions.txt", mode="w")
fp.writelines(json.dumps(questions))
fp.close()

model_answers = [0, 2]

fp = open("model_answers.txt", mode="w")
fp.writelines(json.dumps(model_answers))
fp.close()
