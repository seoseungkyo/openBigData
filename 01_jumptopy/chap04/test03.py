# coding: cp949

def show_candidates():
    f = open("연습생.txt",'r',encoding='UTF8')
    candidate_list = f.read()
    print(candidate_list)
    f.close()

def make_idol():
    f = open('연습생.txt','r',encoding='UTF8')
    while True:
        candidate_list = f.readline()
        if not candidate_list: break
        print("신예 아이돌 "+ candidate_list.splitlines()[0]+" 인기 급 상승")
    f.close()

def make_world_star():
    f = open('연습생.txt','r',encoding='UTF8')
    while True:
        candidate_list = str(f.readline())
        if not candidate_list: break
        print("아이돌 "+ candidate_list.splitlines()[0]+" 월드스타 등극")
    f.close()


show_candidates()
make_idol()
make_world_star()
