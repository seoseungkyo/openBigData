def search_visitor():
    old_name = f.read().lstrip().split()
    for i in old_name:
        if i == new_name:
            print("%s님 다시 방문해주셔서 감사합니다. 즐거운 시간 되세요." %new_name)
            return

    add_visitor()



def add_visitor():
        birth = input("생년 월일을 입력하세요.(예:920517): ")
        f.write(new_name+' '+birth+'\n')
        print("%s님 환영합니다. 아래 내용을 입력하셨습니다." %new_name)
        print(new_name, birth)


f = open('방명록2.txt', 'r+', encoding='UTF-8')
new_name = input("이름을 입력하세요: ")


search_visitor()
