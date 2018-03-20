# coding: cp949

num = input("나이를 입력하세요: ")
age =int(num)

if age>=0 and age<=3:
    print("귀하의 등급은 유아이며, 요금은 무료 입니다")
    
elif age>=4 and age<=13:
    print("귀하의 등급은 어린이이며 요금은 2000원 입니다")
    
elif age>=14 and age<=18:
    print("귀하의 등급은 청소년이며 요금은 3000원 입니다")
    
elif age>=19 and age<=65:
    print("귀하의 등급은 성인이며 요금은 5000원 입니다")
    
elif age>=65:
    print("귀하의 등급은 노인이며 요금은 무료입니다.")
    
else:
    print("다시 입력하세요")
    
