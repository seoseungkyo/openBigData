# coding: cp949

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee=coffee-1
    print("남은 커픠의 양은 %d입니다." %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 중지합니다.")
        break
