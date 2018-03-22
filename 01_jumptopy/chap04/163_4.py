#f = open("E:\\python_workspace\\openBigData\\01_jumptopy\\chap04\\새파일.txt",'r')
f = open("새파일.txt",'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line,end='')
    #줄 바꿔지지 않게 하기~!

f.close()