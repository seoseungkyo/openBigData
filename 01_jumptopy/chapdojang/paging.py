# coding: cp949

m = int(input("총 건수: "))
n = int(input("한페이지 게시물 수: "))

if m == 0:
    print("출력 : 0")

elif m > n:
    print("출력 : %d" %(m/n))

elif m < n:
    print("출력 : %d" %(m))
