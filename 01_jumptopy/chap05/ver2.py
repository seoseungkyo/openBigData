class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self, restaurant_name, cuisine_type):
        print("저희 레스토랑의 명칭은 %s이고 %s전문점입니다" %(self.restaurant_name, self.cuisine_type))
    def open_restaurant(self, restaurant_name):
        print("저희 %s 레스토랑이 오픈했습니다\n" %self.restaurant_name)
    def __del__(self):
        return self.restaurant_name

i=0
list=['중식','한식','분식']

while i<3:
    print("레스토랑 이름과 요리 종류를 선택하세요(공백으로 구분): ")

    res,cui=input().split()
    order = Restaurant(res,cui)
    order.describe_restaurant(res,cui)
    order.open_restaurant(res)
    list[i] = res
    i = i +1
    order = Restaurant(res, cui)

print("저녁 10시가 되었습니다.\n")

print("%s 레스토랑 문 닫습니다" %(list[0]))
print("%s 레스토랑 문 닫습니다" %(list[1]))
print("%s 레스토랑 문 닫습니다" %(list[2]))


