# coding: cp949

my_nba_players={"��Ŭ��ȣ��":"�ؽ��","��罺����Ʈ":"Ŀ��","��Ʋ����":"�����","������":"���","Ŭ������":"�����","����Ŀ��":"������","���ø�����":"���̺�","�޽���":"�ϵ�"}

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
print("step 4, trying to search character of '��Ŭ��ȣ��' in the my_nba_players dictionary")

print("\n")
if '��Ŭ��ȣ��' in my_nba_players:
    for player_key in my_nba_players.keys():
        print(player_key)
        if player_key == '��Ŭ��ȣ��':
            print("i found ��Ŭ��ȣ�� now, i will tell you about him")
            print("He is a "+ my_nba_players['��Ŭ��ȣ��']+"player")
            break;
