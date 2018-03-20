# coding: cp949
#a=[(1,2),(3,4),(5,6)]
#for (first,last) in a:
#    print(first+last)

student_name_list=[
        ('유','영재'),
        ('서','승교'),
        ('김','종우'),
        ('이','효진'),
        ('문','재인'),
        ('문','희식')]


name = input("성 입력: ")
print(name)
is_found_flag=False
for (last_name, first_name) in student_name_list:
    if name==last_name:
        if is_found_flag == False:
            print("\n검색결과")
            is_found_flag=True
        print(last_name+first_name)
    
 
