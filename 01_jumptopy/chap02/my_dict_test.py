# coding: cp949

my_nba_players={"오클라호마":"앤써니","골든스테이트":"커리","포틀랜드":"릴라드","보스턴":"어빙","클리블랜드":"르브론","레이커스":"론조볼","뉴올리언즈":"데이비스","휴스턴":"하든"}

print(my_nba_players)
print("\n")
print("step 1, printing the raw type of dictionary, 'my_nba_players'")
print(my_nba_players)

print("\n")
print("step 2, printing the key lists using my_nba_players.keys() fun")
print(my_nba_players.keys())

print("\n")
print("step 3, printing the value lists using my_nba_players.values() fun")
print(my_nba_players.values())

print("\n")
print("step 4, trying to search character of '오클라호마' in the my_nba_players dictionary")

print("\n")
if '오클라호마' in my_nba_players:
    for player_key in my_nba_players.keys():
        print(player_key)
        if player_key == '오클라호마':
            print("i found 오클라호마 now, i will tell you about him")
            print("He is a "+ my_nba_players['오클라호마']+"player")
            break;
