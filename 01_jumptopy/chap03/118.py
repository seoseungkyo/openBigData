# coding: cp949

#pocket = ['paper','cellphone','money']
pocket = []

item = input("���Ͽ� ������ ì�⼼��: ")
pocket.append(item)

if 'card' in pocket:
    print("card��õ")
elif 'money' in pocket:
    print("money")
elif 'cellphone' in pocket:
    print("cellphone")
else:
    print("walk")

