f=open("sample.txt")
lines=f.readlines()
print(lines)
f.close()

total=0
count = 0
for line in lines:
    score= line
    total = total + int(score)
    count = count + 1
average =  total / count
print(average)
print(total)
print(count)
f = open("result.txt",'w' )
data = "평균은 %d\n총합은 %s" %(average, total)
f.write(data)
f.close()