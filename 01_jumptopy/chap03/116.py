#coding: cp949


x=1
y=0
z=0

#print("x,y,z 입력")

#x = int(input("x= "))
#y = int(input("y= "))
#z = int(input("x= "))

input_str="x={1} y={2} z={3}".format(x,y,z)
print(input_str)
print("x={0} y={1} z={1}".format(x,y,z))

if x or y:
    print("if xory만족")
else:
    print("or 불만족")

if x and y:
    print("if xandy만족")
else:
    print("and 불만족")

if not x:
    print("not x 만족")
else:
    print("not x 불만족")

if not y:
    print("noty 만족")
else:
    print("noty 불만족")


if x and y and z:
    print("and and 만족")
else:
    print("and and 불만족")

if x or y or z:
    print("or or 만족")
else:
    print("or or 불만족")









