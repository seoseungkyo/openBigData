# coding: cp949

def show_candidates():
    f = open("������.txt",'r',encoding='UTF8')
    candidate_list = f.read()
    print(candidate_list)
    f.close()

def make_idol():
    f = open('������.txt','r',encoding='UTF8')
    while True:
        candidate_list = f.readline()
        if not candidate_list: break
        print("�ſ� ���̵� "+ candidate_list.splitlines()[0]+" �α� �� ���")
    f.close()

def make_world_star():
    f = open('������.txt','r',encoding='UTF8')
    while True:
        candidate_list = str(f.readline())
        if not candidate_list: break
        print("���̵� "+ candidate_list.splitlines()[0]+" ���彺Ÿ ���")
    f.close()


show_candidates()
make_idol()
make_world_star()
