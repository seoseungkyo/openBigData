class Restaurant:
    f= open("고객서빙현황로그.txt",'r')
    number_served = int(f.readline())
    todays_customer = 0
    f.close()
    newf= open("고객서빙현황로그.txt", 'w')

    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self, restaurant_name, cuisine_type):
        print("저희 레스토랑의 명칭은 %s이고 %s전문점입니다" %(self.restaurant_name, self.cuisine_type))
    def open_restaurant(self, restaurant_name):
        print("저희 %s 레스토랑이 오픈했습니다" %self.restaurant_name)
    def reset_number_served(self):
        self.todays_customer = 0
    def increment_number_served(self,number):
        self.todays_customer =  self.todays_customer + number
    def check_customer_number(self):
        return self.todays_customer
    def __del__(self):
        print("총 사람: %d" % (self.number_served + self.todays_customer))
        data = self.todays_customer + self.number_served
        newf.write(data)
        newf.close(0)
        return self.number_served + self.todays_customer


print("레스토랑 이름과 요리 종류를 선택하세요(공백으로 구분): ")
res,cui=input().split()
order = Restaurant(res,cui)
order.describe_restaurant(res,cui)
order.open_restaurant(res)

while True:
    chk = input("어서오세요 몇명이십니까?(초기화:0, 종료=-1, 누적고객확인:p)" )
    if  chk=='p':
        print("지금까지 총 %d명 오셨습니다."%(order.check_customer_number()))
    elif chk=='-1':
        print("%s 식당 문 닫습니다" %res)
        break
    elif chk=='0':
        order.reset_number_served()
        print("손님 카운팅을 0으로 초기화 하였습니다.")
    else:
        print("손님 %d명 오셨습니다. 자리를 안내해 드리겠습니다"%int(chk))
        order.increment_number_served(int(chk))