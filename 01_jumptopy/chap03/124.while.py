# coding: cp949

prompt="""
1. 추가
2. 삭제
3. 리스트
4. 종료

숫자를 입력하세요: """
number=0
while number !=4:
    number = int(input(prompt))
    if number==1:
        print("추가 메뉴 선택하셨습니다")
    elif number==2:
        print("삭제 메뉴 선택하셨습니다")
    elif number==3:
        print("리스트 메뉴 선택하셨습니다")
    elif number==4:
        print("종료합니다")
        break
    else:
        print("1234메뉴만 지원합니다")
