def fib(n):
    i = 0
    j = 1
    result = 0
    while result <= int(n):
        print(result,end=',')
        result = i+j
        i = j
        j = result



num = input("입력: ")
fib(num)
print("...")