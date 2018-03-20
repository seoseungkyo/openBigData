# coding: cp949


num = input("줄 수를 입력하시오(0 <- 종료): ")
line=int(num)

while True:
    if line%2 !=0:
        for star in range(0,line):     
            print(" "*(line-star)+"*"*(2*star-1))
        break  
    else:
        break


