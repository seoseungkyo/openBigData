# coding: cp949

#pocket = ['paper','cellphone','money']
pocket = []

item = input("포켓에 아이템 챙기세요: ")
pocket.append(item)

if 'card' in pocket:
    print("card추천")
elif 'money' in pocket:
    print("money")
elif 'cellphone' in pocket:
    print("cellphone")
else:
    print("walk")

