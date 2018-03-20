# coding: cp949


d = input("출력하고자 하는 단을 입력하세요: ")

for d in range(d,d+1):
    print("%d 단" %d)
    for j in range(1,10):
        print("%d X %d = %d"%(d, j, d*j))
    print('')
