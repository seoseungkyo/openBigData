import sys
usernames = sys.argv[1:]
def greet_users(usernames):
    for i in usernames:
        print("hello, " +i[0].upper()+i[1:], end='!  ')
greet_users(usernames)


