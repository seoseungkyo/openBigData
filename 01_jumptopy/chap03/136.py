# coding: cp949


d = input("����ϰ��� �ϴ� ���� �Է��ϼ���: ")

for d in range(d,d+1):
    print("%d ��" %d)
    for j in range(1,10):
        print("%d X %d = %d"%(d, j, d*j))
    print('')
