# coding: cp949

#money = 2000


#print("���� ���� �Է��ϼ���")

#money=int(input())

money=int(input("�������� �ݾ��� �Է��ϼ���: "))
card = int(input("ī�带 �����ϰ� ��ʴϱ�?1:�� 2:�ƴϿ�"))

print("\n���� ���� ����"+str(money)+"�Դϴ�")
if card==1:
    print("���� �ſ�ī�� �ֽ��ϴ�")
else:
    print("\���� �ſ�ī�� �����ϴ�")


print("\n�м����\n")

if money>=3000 or card==1:
    print("�ýø� Ż �� �ֽ��ϴ�")
else:
    print("�ýø� Ż �� �����ϴ�")

print("\n�����մϴ�")
