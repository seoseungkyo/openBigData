# coding: cp949

nc = 3
dc = 5
nc_count = 0
dc_count = 0
price = 0

while True:
    num = input("���̸� �Է��ϼ���: ")
    age =int(num)
    nc_count = nc_count + 1
    dc_count = dc_count + 1    
    
    if age<0:
        print("�ٽ� �Է��ϼ���: ")
        continue

    elif age<=3:
        print("������ ����� �����̸� ����� �����Դϴ�.")
        nc_count = nc_count -1
        dc_count = dc_count -1
        continue

    elif age<=13:
        price = 2000
        grade = "���"
           
    elif age<=18:
        price = 3000
        grade = "û�ҳ�"
          
    elif age<=59:
        price = 5000
        grade = "����"

    elif age<=65:
        price = 5000
        grade = "���"

    elif age>=66:
        print("������ ����� �����̸� ����� �����Դϴ�.")
        nc_count = nc_count -1
        dc_count = dc_count -1
        continue

    
    print("������ ����� %s�̸� ����� %d�� �Դϴ�" %(grade,price))
    check = input("��� ������ �����ϼ���. 1:���� 2:���� ���� �ſ� ī�� => ")

    if check == '1':
        money = int(input("����� �Է��ϼ��� => "))
        if money == price:
            print("�����մϴ�. Ƽ���� �����մϴ�.")
        elif money >= price:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�" %(money-price))
        elif money < price:
            print("%d����  ���ڶ��ϴ�. %d���� ��ȯ�մϴ�" %((price-money),money))
            nc_count = nc_count - 1
            dc_count = dc_count - 1
    elif check =='2':  
        if grade == "���":
            print("������ ����� %s�̸� ����� %d�� �Դϴ�. �����Ǿ����ϴ�." %(grade,price * 0.9*0.95))
        else:
            print("������ ����� %s�̸� ����� %d�� �Դϴ�. �����Ǿ����ϴ�." %(grade,price * 0.9))

    
    if nc != 0 and nc_count >=7 and nc_count % 7 ==0:
        nc = nc -1
        print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ����Ƽ���� �����մϴ�. �ܿ� ���� Ƽ�� : %d�� " %nc )
    elif dc != 0 and dc_count >= 4 and nc_count % 4 == 0:
        dc = dc -1
        print("�����մϴ�. ���� ȸ���� ���� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� Ƽ���� �����մϴ�. �ܿ� ���� Ƽ�� : %d�� " %dc )
