# coding: cp949

prompt="""
1. �߰�
2. ����
3. ����Ʈ
4. ����

���ڸ� �Է��ϼ���: """
number=0
while number !=4:
    number = int(input(prompt))
    if number==1:
        print("�߰� �޴� �����ϼ̽��ϴ�")
    elif number==2:
        print("���� �޴� �����ϼ̽��ϴ�")
    elif number==3:
        print("����Ʈ �޴� �����ϼ̽��ϴ�")
    elif number==4:
        print("�����մϴ�")
        break
    else:
        print("1234�޴��� �����մϴ�")
