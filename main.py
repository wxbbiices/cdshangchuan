#此代码适用于OPPO Reno9 微信输入法进行测试
import os
import time
import random

for i in range(820089,820801):
    erhao='adb shell input text CR034223'+str(i)
    #体重数据
    tizhong = random.uniform(115, 130)
    set_tizhong = round(tizhong, 1)
    #体长数据
    tichang = random.uniform(105, 125)
    set_tichang = round(tichang, 0)
    #腹垂数据
    fuchui = random.uniform(39, 42)
    set_fuchui = round(fuchui, 0)
    #P1数据
    pone = random.uniform(18, 25)
    set_pone = round(pone, 1)
    mlpone = 'adb shell input text' + str(set_pone)
    #P2P3数据
    ptwo = random.uniform(8, 15)
    set_ptwo = round(ptwo, 1)
    pthree = random.uniform(10, 16)
    set_ptheee = round(pthree, 1)
    if set_ptwo == set_ptheee:
        set_ptheee = set_ptwo + 1
        set_ptwo = set_ptwo
    if set_ptwo > set_ptheee:
        set_ptheee, set_ptwo = set_ptwo, set_ptheee

    mltizhong = 'adb shell input text ' + str(set_tizhong)
    mltichang = 'adb shell input text ' + str(set_tichang)
    mlfuchui = 'adb shell input text ' + str(set_fuchui)
    mlpone = 'adb shell input text ' + str(set_pone)
    mlptwo = 'adb shell input text ' + str(set_ptwo)
    mlpthree = 'adb shell input text ' + str(set_ptheee)

    os.system('adb shell input tap 506 1416')  # 点击耳牌号位置
    os.system(erhao)#输入耳号
    time.sleep(10)
    os.system('adb shell input tap 807 1353')  # 点击结测
    time.sleep(5)
    os.system('adb shell input tap 896 796')  # 点击栏位
    time.sleep(3)
    os.system('adb shell input tap 1011 1080')#退出栏位
    time.sleep(2)
    os.system('adb shell input tap 798 1048')#点击体重
    os.system(mltizhong)  # 输入体重
    time.sleep(1)
    os.system('adb shell input tap 590 1155')  # 点击P1
    os.system(mlpone)  # 输入P1
    time.sleep(1)
    os.system('adb shell input tap 951 2210')  # 点击P2
    os.system(mlptwo)  # 输入P2
    time.sleep(1)
    os.system('adb shell input tap 951 2210')  # 移动到P3
    os.system(mlpthree)  # 输入P3
    time.sleep(1)
    os.system('adb shell input tap 951 2210')
    os.system('adb shell input tap 951 2210')
    os.system('adb shell input tap 951 2210')  # 三次移动到体长
    os.system(mltichang)  # 输入体长
    time.sleep(1)
    os.system('adb shell input tap 951 2210')  # 移动到腹垂
    os.system(mlfuchui)  # 输入腹垂
    time.sleep(1)
    os.system('adb shell input tap 951 2210')  # 移动到题型评分
    os.system('adb shell input tap 858 1446')  # 选择四星
    os.system('adb shell input tap 99 2326')  # 退出键盘
    time.sleep(1)
    os.system('adb shell input tap 595 2238')  # 点击保存
    time.sleep(6)
    os.system('adb shell input tap 795 1350')  # 点击进行下一个
    time.sleep(6)