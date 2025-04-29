import statistics
score = []
typing = True
while typing:
    name = input("請輸入學生姓名(結束程式請輸入p)：")
    if name == "p":
        typing = False
        break
    grade = int(input(f"請輸入{name}的成績："))
    score.append([name, grade])

print(f"平均分數為：{statistics.mean([x[1] for x in score])}")
print("及格名單：[", end = ' ')
for i in score:
    if i[1] >= 60:
        print(i[0],end =' ')
print("]")