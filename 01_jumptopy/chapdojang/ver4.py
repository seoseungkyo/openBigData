# coding: cp949

num = input("���̸� �Է��ϼ���: ")
age =int(num)



if age>=0 and age<=3:
    print("������ ����� �����̸�, ����� ���� �Դϴ�")
elif age>=4 and age<=13:
    print("������ ����� ����̸� ����� 2000�� �Դϴ�")
    check = input("��� ������ �����ϼ���. 1:���� 2:���� ���� �ſ� ī�� => ")
    if check == '1':
        money = int(input("����� �Է��ϼ���"))
        if money == 2000:
            print("�����մϴ�. Ƽ���� �����մϴ�.")
        elif money >= 2000:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�" %(money-2000))
        elif money < 2000:
            print("%d����  ���ڶ��ϴ�. %d���� ��ȯ�մϴ�" %((2000-money),money))
    elif check =='2':
            print("������ ����� ����̸� ����� 1800�� �Դϴ�. �����Ǿ����ϴ�")
        


elif age>=14 and age<=18:
        print("������ ����� û�ҳ��̸� ����� 3000�� �Դϴ�")
        check = input("��� ������ �����ϼ���. 1:���� 2:���� ���� �ſ� ī�� => ")
        if check == '1':
            money = int(input("����� �Է��ϼ���"))
            if money == 3000:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            elif money >= 3000:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�" %(money-2000))
            elif money < 3000:
                print("%d����  ���ڶ��ϴ�. %d���� ��ȯ�մϴ�" %((2000-money),money))
        elif check =='2':
            print("������ ����� ����̸� ����� 2700�� �Դϴ�. �����Ǿ����ϴ�")
        
elif age>=19 and age<=65: 
    if age >= 19 and age < 60:
        print("������ ����� �����̸� ����� 5000�� �Դϴ�")
        check = input("��� ������ �����ϼ���. 1:���� 2:���� ���� �ſ� ī�� => ")
        if check == '1':
            money = int(input("����� �Է��ϼ���"))
            if money == 5000:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            elif money >= 5000:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�" %(money-5000))
            elif money < 5000:
                print("%d����  ���ڶ��ϴ�. %d���� ��ȯ�մϴ�" %((5000-money),money))
        elif check =='2':
            print("������ ����� �����̸�, ����� 4500�� �Դϴ�. �����Ǿ����ϴ�")
    elif age>=60 and age <=65:
        print("������ ����� ����̸� ����� 5000�� �Դϴ�")
        check = input("��� ������ �����ϼ���. 1:���� 2:��������ſ�ī�� => ")
        if check == '1':
            money = int(input("����� �Է��ϼ���"))
            if money == 5000:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            elif money >= 5000:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�" %(money-5000))
            elif money < 5000:
                print("%d����  ���ڶ��ϴ�. %d���� ��ȯ�մϴ�" %((5000-money),money))
        elif check =='2':
            print("������ ����� ����̸�, ����� 4250�� �Դϴ�. �����Ǿ����ϴ�")
elif age>=66:
        print("������ ����� �����̸� ����� �����Դϴ�.")
    
else:
        print("�ٽ� �Է��ϼ���")
  