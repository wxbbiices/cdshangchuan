
#本代码配合微信输入法使用
import os
import time

#os.system('adb shell input tap 506 1416')#点击耳牌号位置
#os.system('adb shell input text CR034223820008')#输入耳牌号
#time.sleep(1)
#os.system('adb shell input tap 807 1353')#点击结测
#time.sleep(2)
os.system('adb shell input tap 896 796')#点击栏位
time.sleep(3)
os.system('adb shell input tap 1011 1080')#退出栏位
time.sleep(2)
os.system('adb shell input tap 798 1048')#点击体重
os.system('adb shell input text 115')#输入体重
time.sleep(1)
os.system('adb shell input tap 590 1155')#点击P1
os.system('adb shell input text 21.1')#输入P1
time.sleep(1)
os.system('adb shell input tap 951 2210')#点击P2
os.system('adb shell input text 13.1')#输入P2
time.sleep(1)
os.system('adb shell input tap 951 2210')#移动到P3
os.system('adb shell input text 15.1')#输入P3
time.sleep(1)
os.system('adb shell input tap 951 2210')
os.system('adb shell input tap 951 2210')
os.system('adb shell input tap 951 2210')#三次移动到体重
os.system('adb shell input text 121')#输入体重
time.sleep(1)
os.system('adb shell input tap 951 2210')#移动到腹垂
os.system('adb shell input text 40')#输入腹垂
time.sleep(1)
os.system('adb shell input tap 951 2210')#移动到题型评分
os.system('adb shell input tap 858 1446')#选择四星
os.system('adb shell input tap 99 2326')#退出键盘
time.sleep(1)
#os.system('adb shell input tap 595 2238')#点击保存
time.sleep(1)
os.system('adb shell input tap 795 1350')#点击进行下一个