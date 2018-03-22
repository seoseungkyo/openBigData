ingredient_list = []
def input_ingredient():
    while True:
        ingredient = input("안녕하세요. 원하시는 재료를 입력하세요: ")
        ingredient_list.append(ingredient)
        if ingredient == '종료':
            break
        else:
            continue
        return ingredient_list

def make_sandwiches():
    print("\n샌드위치를 만들겠습니다.")
    for i in ingredient_list:
        print(i + "를 추가합니다.")

order = int(input("안녕하세요 저희 가게에 방문해주셔서 감사합니다.\n1. 주문\n2. 종료\n입력: "))
if order == 1:
    input_ingredient()
    make_sandwiches()
    print(".\n.\n.\n 여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요")
elif order ==2:
    print("종료")
