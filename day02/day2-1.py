import math
from math import floor
print("成績判斷系統是也！")
print("請輸入成績，輸入負數結束程式")
while True:
    user_input = input("請輸入成績：")
    try:
        user_input = int(user_input)
        grade = floor(int(user_input)/10)
        match (grade):
            case 10|9:
                print("A等")
            case 8:
                print("B等")
            case 7:
                print("C等")
            case 6:
                print("D等")
            case 5|4|3|2|1|0:
                print("不及格")
            case _:
                print("辛苦啦")
                break
    except ValueError:
        print("不要亂輸啦！")