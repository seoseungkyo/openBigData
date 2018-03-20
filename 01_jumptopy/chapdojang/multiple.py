

n = 1
m = 1
sum = 0

while True:
    if n*3 < 1000:
        sum = sum + 3*n
        n = n + 1

    if m*5 < 1000:    
        sum = sum + 5*m
        m = m + 1
    
    if n*3 >=1000:
        break


print(sum)

