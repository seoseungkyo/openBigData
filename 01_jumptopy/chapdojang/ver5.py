# coding: cp949

nc = 3
dc = 5
nc_count = 0
dc_count = 0
price = 0

while True:
    num = input("나이를 입력하세요: ")
    age =int(num)
    nc_count = nc_count + 1
    dc_count = dc_count + 1    
    
    if age<0:
        print("다시 입력하세요: ")
        continue

    elif age<=3:
        print("귀하의 등급은 유아이며 요금은 무료입니다.")
        nc_count = nc_count -1
        dc_count = dc_count -1
        continue

    elif age<=13:
        price = 2000
        grade = "어린이"
           
    elif age<=18:
        price = 3000
        grade = "청소년"
          
    elif age<=59:
        price = 5000
        grade = "성인"

    elif age<=65:
        price = 5000
        grade = "장년"

    elif age>=66:
        print("귀하의 등급은 노인이며 요금은 무료입니다.")
        nc_count = nc_count -1
        dc_count = dc_count -1
        continue

    
    print("귀하의 등급은 %s이며 요금은 %d원 입니다" %(grade,price))
    check = input("요금 유형을 선택하세요. 1:현금 2:공원 전용 신용 카드 => ")

    if check == '1':
        money = int(input("요금을 입력하세요 => "))
        if money == price:
            print("감사합니다. 티켓을 발행합니다.")
        elif money >= price:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" %(money-price))
        elif money < price:
            print("%d원이  모자랍니다. %d원을 반환합니다" %((price-money),money))
            nc_count = nc_count - 1
            dc_count = dc_count - 1
    elif check =='2':  
        if grade == "장년":
            print("귀하의 등급은 %s이며 요금은 %d원 입니다. 결제되었습니다." %(grade,price * 0.9*0.95))
        else:
            print("귀하의 등급은 %s이며 요금은 %d원 입니다. 결제되었습니다." %(grade,price * 0.9))

    
    if nc != 0 and nc_count >=7 and nc_count % 7 ==0:
        nc = nc -1
        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 무료티켓을 발행합니다. 잔여 무료 티켓 : %d장 " %nc )
    elif dc != 0 and dc_count >= 4 and nc_count % 4 == 0:
        dc = dc -1
        print("축하합니다. 연관 회원권 구매 이벤트에 당첨되었습니다. 할인 티켓을 발행합니다. 잔여 무료 티켓 : %d장 " %dc )
