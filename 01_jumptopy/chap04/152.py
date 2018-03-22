def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나의 나이는 %d살입니다." %old)
    if man:
        print("man")
    else:
        print("woman")


say_myself("박응용",27)
say_myself("박응용",56,True)
say_myself("박응용",36,False)