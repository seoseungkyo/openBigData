# coding: cp949


num = input("�� ���� �Է��Ͻÿ�(0 <- ����): ")
line=int(num)

while True:
    if line%2 !=0:
        for star in range(0,line):     
            print(" "*(line-star)+"*"*(2*star-1))
        break  
    else:
        break


