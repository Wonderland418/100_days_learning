import random
# 1. 隨機產生一個 1~100 的整數，並讓使用者猜測這個數字
play = True
while play:
    secret = random.randint(1, 100)
    num = -2
    while num != secret:
        num = input("請輸入一個1-100的數字：")
        while True:        
            try:
                int(num)
            except ValueError:
                num = input("不要亂來啦，給我重輸窩：")
                continue
            if int(num) < 1 or int(num) > 100:
                num = input("不要亂來啦，給我重輸窩：")
                continue
            else:
                break
        num = int(num)
        if num < secret:
            print("猜的數字小了")
        elif num > secret:
            print("猜的數字大了")
        else:
            print("恭喜你，猜對了！")
            break
    # 2. 提示使用者是否要再玩一次
    # 3. 如果使用者輸入yes，則重新開始遊戲；如果輸入no，則結束遊戲
    print("======================")
    while True:
        continue_or_not = input("再來一局嗎?(y/n):")
        if continue_or_not == "y":
            play = True
            print("好耶！")
            print("======================")
            break
        elif continue_or_not == "n":
            play = False
            print("謝謝遊玩")
            break
        else:
            print("蛤？你給我再好好說一次喔？") 
            continue
    
