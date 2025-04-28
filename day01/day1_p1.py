import math
from math import floor
print("請輸入兩個數字")
A = int(input("第一個數字："))
B = int(input("第二個數字："))
while True:
    print("請輸入你要的運算")
    print("1.加法 2.減法 3.乘法 4.除法 5.結束運算")
    sel = input()
    match sel:
        case "1":
            print("A + B = ", A + B)
        case "2":
            print("A - B = ", A - B)
        case "3":
            print("A X B = ", A * B)
        case "4":
            print("A ÷ B = ", floor(A / B) , " ... ", A % B)
        case "5":
            break