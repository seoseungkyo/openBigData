# coding: cp949

num = input("���̸� �Է��ϼ���: ")
age =int(num)
if age>=0 and age<=3:
    print("����� ���� �Դϴ�")
elif age>=4 and age<=13:
    print("����� 2000�� �Դϴ�")
elif age>=14 and age<=18:
    print("����� 3000�� �Դϴ�")
elif age>=19 and age<=65:
    print("����� 5000�� �Դϴ�")
else:
    print("����� �����Դϴ�.")
