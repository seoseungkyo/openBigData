#coding: cp949


x=1
y=0
z=0

#print("x,y,z �Է�")

#x = int(input("x= "))
#y = int(input("y= "))
#z = int(input("x= "))

input_str="x={1} y={2} z={3}".format(x,y,z)
print(input_str)
print("x={0} y={1} z={1}".format(x,y,z))

if x or y:
    print("if xory����")
else:
    print("or �Ҹ���")

if x and y:
    print("if xandy����")
else:
    print("and �Ҹ���")

if not x:
    print("not x ����")
else:
    print("not x �Ҹ���")

if not y:
    print("noty ����")
else:
    print("noty �Ҹ���")


if x and y and z:
    print("and and ����")
else:
    print("and and �Ҹ���")

if x or y or z:
    print("or or ����")
else:
    print("or or �Ҹ���")









