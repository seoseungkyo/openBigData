#f = open("E:\\python_workspace\\openBigData\\01_jumptopy\\chap04\\새파일.txt",'r')
f = open("새파일.txt",'w')

for i in range(11,20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()