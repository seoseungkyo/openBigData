# coding: cp949
#a=[(1,2),(3,4),(5,6)]
#for (first,last) in a:
#    print(first+last)

student_name_list=[
        ('��','����'),
        ('��','�±�'),
        ('��','����'),
        ('��','ȿ��'),
        ('��','����'),
        ('��','���')]


name = input("�� �Է�: ")
print(name)
is_found_flag=False
for (last_name, first_name) in student_name_list:
    if name==last_name:
        if is_found_flag == False:
            print("\n�˻����")
            is_found_flag=True
        print(last_name+first_name)
    
 
