# coding: cp949

#money = 2000


#print("가진 돈을 입력하세요")

#money=int(input())

money=int(input("가지고계신 금액을 입력하세요: "))
card = int(input("카드를 소유하고 계십니까?1:예 2:아니요"))

print("\n현재 가진 돈은"+str(money)+"입니다")
if card==1:
    print("현재 신용카드 있습니다")
else:
    print("\현재 신용카드 없습니다")


print("\n분석결과\n")

if money>=3000 or card==1:
    print("택시를 탈 수 있습니다")
else:
    print("택시를 탈 수 없습니다")

print("\n감사합니다")
