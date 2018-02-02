# _*_ coding: utf-8 _*_
# by:Snowkingliu
# 2018/2/1 上午10:42
import json

asking_report = [
    # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    # [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    # [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    # [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    # [1, 1],
    # [0, 2]s
]

asking_user_info = [
    # {"user": "Mellon0", "avatar_url": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqY2Z0bpmlYeGNZKq4nB7MowHHiciba6H6aiarWbJkBtbjgcncOLIfXI2ve7fuga0Gfoib54hGb8hYib8A/0"},
    # {"user": "Mellon1", "avatar_url": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqY2Z0bpmlYeGNZKq4nB7MowHHiciba6H6aiarWbJkBtbjgcncOLIfXI2ve7fuga0Gfoib54hGb8hYib8A/0"}
                       # {"user": "Mellon0", "avatar_url": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqY2Z0bpmlYeGNZKq4nB7MowHHiciba6H6aiarWbJkBtbjgcncOLIfXI2ve7fuga0Gfoib54hGb8hYib8A/0"},
                       # {"user": "Mellon1", "avatar_url": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqY2Z0bpmlYeGNZKq4nB7MowHHiciba6H6aiarWbJkBtbjgcncOLIfXI2ve7fuga0Gfoib54hGb8hYib8A/0"},
                       # {"user": "Mellon2", "avatar_url": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqY2Z0bpmlYeGNZKq4nB7MowHHiciba6H6aiarWbJkBtbjgcncOLIfXI2ve7fuga0Gfoib54hGb8hYib8A/0"},
                       # {"user": "Mellon3", "avatar_url": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqY2Z0bpmlYeGNZKq4nB7MowHHiciba6H6aiarWbJkBtbjgcncOLIfXI2ve7fuga0Gfoib54hGb8hYib8A/0"},
]

fp = open("asking_report.txt", mode="w")
fp.writelines(json.dumps(asking_report))
fp.close()

fp = open("asking_user_info.txt", mode="w")
fp.writelines(json.dumps(asking_user_info))
fp.close()
