# coding: cp949



#i=0
#marks=[0,0,0,0,0]
#while i < len(marks):
#    print("%d�� �л��� ������ �Է��ϼ���:" %(i+1))
#    marks[i] = int(input())
#    i=i+1#
#
#print(marks)
#i=0
#for mark in marks:#

#    if mark > 60:
#        print("%d�� �л��� ������ %d�� �Դϴ�. �հ��Դϴ�" %((i+1),mark))
#        i=i+1
#    else:
#        print("%d�� �л��� ������ %d�� �Դϴ�. ���հ��Դϴ�" %((i+1),mark))

marks = []
number = 1
while number<=5:
    mark = input(str(number)+"�� �л� ���� �Է�:")
    marks.append(int(mark))
    number=number+1

number =1
for mark in marks:
    if mark>60:
        print("%d�� �л� %d��, �հ��Դϴ�"%(number,mark))
    else:
        print("%d�� �л� %d��, ���հ��Դϴ�"%(number,mark))

    number=number+1
