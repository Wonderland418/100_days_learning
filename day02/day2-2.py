import math
from math import floor
print("早安哇")
print("你竟然想來算數學嗎？")
print("好哇，那就來哇！")
print("========================")

while True:
    num1 = input("請輸入第一個數字: ")
    while True:
        try:
            num1 = int(num1)
            break
        except ValueError:
            num1 = input("請重新輸入第一個數字: ")
    num2 = input("請輸入第二個數字: ")
    while True:
        try:
            num2 = int(num2)
            break
        except ValueError:
            num2 = input("請重新輸入第二個數字: ")
    
    print("========================")
    print("若要進行加法請輸入1")
    print("若要進行減法請輸入2")
    print("若要進行乘法請輸入3")
    print("若要進行除法請輸入4")
    print("========================")
    
    operator = input("請選擇運代碼: ")
    print()
    match operator:
        case "1":
            print(f"{num1} + {num2} = {num1 + num2}")
        case "2":
            print(f"{num1} - {num2} = {num1 - num2}")
        case "3":
            print(f"{num1} * {num2} = {num1 * num2}")
        case "4":
            if num2 == 0:
                print("除數不能為0")
            else:
                print(f"{num1} / {num2} = {floor(num1 / num2)} ... {num1 % num2}")
        case _:
            print("無效的運算代碼")
    
    print("========================")
    print("若要繼續請輸入0")
    print("若要結束請任意輸入")
    continue_or_not = input("")

    if continue_or_not == "0":
        print("=======================")
        continue
    else:
        print("銘謝惠顧囉~")
        break
    