# coding: cp949



#i=0
#marks=[0,0,0,0,0]
#while i < len(marks):
#    print("%d번 학생의 점수를 입력하세요:" %(i+1))
#    marks[i] = int(input())
#    i=i+1#
#
#print(marks)
#i=0
#for mark in marks:#

#    if mark > 60:
#        print("%d번 학생의 점수는 %d점 입니다. 합격입니다" %((i+1),mark))
#        i=i+1
#    else:
#        print("%d번 학생의 점수는 %d점 입니다. 불합격입니다" %((i+1),mark))

marks = []
number = 1
while number<=5:
    mark = input(str(number)+"번 학생 점수 입력:")
    marks.append(int(mark))
    number=number+1

number =1
for mark in marks:
    if mark>60:
        print("%d번 학생 %d점, 합격입니다"%(number,mark))
    else:
        print("%d번 학생 %d점, 불합격입니다"%(number,mark))

    number=number+1
