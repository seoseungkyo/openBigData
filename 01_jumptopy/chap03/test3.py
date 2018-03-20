# coding: cp949


line=int(input("홀수를 입력하시오 (0<- 종료): "))
num=int(line/2)+1

for i in range(1,line+1):

    if i<=num:

        print(' '*(line-i-num+1)+'*'*i + '*'*(i-1))

    else :

        print(' '*(i-num)+'*'*((line*2)-(i*2)+1))

