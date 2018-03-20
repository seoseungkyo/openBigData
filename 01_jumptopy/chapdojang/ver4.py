# coding: cp949

num = input("나이를 입력하세요: ")
age =int(num)



if age>=0 and age<=3:
    print("귀하의 등급은 유아이며, 요금은 무료 입니다")
elif age>=4 and age<=13:
    print("귀하의 등급은 어린이이며 요금은 2000원 입니다")
    check = input("요금 유형을 선택하세요. 1:현금 2:공원 전용 신용 카드 => ")
    if check == '1':
        money = int(input("요금을 입력하세요"))
        if money == 2000:
            print("감사합니다. 티켓을 발행합니다.")
        elif money >= 2000:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" %(money-2000))
        elif money < 2000:
            print("%d원이  모자랍니다. %d원을 반환합니다" %((2000-money),money))
    elif check =='2':
            print("귀하의 등급은 어린이이며 요금은 1800원 입니다. 결제되었습니다")
        


elif age>=14 and age<=18:
        print("귀하의 등급은 청소년이며 요금은 3000원 입니다")
        check = input("요금 유형을 선택하세요. 1:현금 2:공원 전용 신용 카드 => ")
        if check == '1':
            money = int(input("요금을 입력하세요"))
            if money == 3000:
                print("감사합니다. 티켓을 발행합니다.")
            elif money >= 3000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" %(money-2000))
            elif money < 3000:
                print("%d원이  모자랍니다. %d원을 반환합니다" %((2000-money),money))
        elif check =='2':
            print("귀하의 등급은 어린이이며 요금은 2700원 입니다. 결제되었습니다")
        
elif age>=19 and age<=65: 
    if age >= 19 and age < 60:
        print("귀하의 등급은 성인이며 요금은 5000원 입니다")
        check = input("요금 유형을 선택하세요. 1:현금 2:공원 전용 신용 카드 => ")
        if check == '1':
            money = int(input("요금을 입력하세요"))
            if money == 5000:
                print("감사합니다. 티켓을 발행합니다.")
            elif money >= 5000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" %(money-5000))
            elif money < 5000:
                print("%d원이  모자랍니다. %d원을 반환합니다" %((5000-money),money))
        elif check =='2':
            print("귀하의 등급은 성인이며, 요금은 4500원 입니다. 결제되었습니다")
    elif age>=60 and age <=65:
        print("귀하의 등급은 장년이며 요금은 5000원 입니다")
        check = input("요금 유형을 선택하세요. 1:현금 2:공원전용신용카드 => ")
        if check == '1':
            money = int(input("요금을 입력하세요"))
            if money == 5000:
                print("감사합니다. 티켓을 발행합니다.")
            elif money >= 5000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" %(money-5000))
            elif money < 5000:
                print("%d원이  모자랍니다. %d원을 반환합니다" %((5000-money),money))
        elif check =='2':
            print("귀하의 등급은 장년이며, 요금은 4250원 입니다. 결제되었습니다")
elif age>=66:
        print("귀하의 등급은 노인이며 요금은 무료입니다.")
    
else:
        print("다시 입력하세요")
  
