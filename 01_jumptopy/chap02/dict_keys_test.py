# coding: cp949
#-*- coding: utf-8 -*-
#player={"�迬��":"�ǰ�","������":"�߱�","������":"�౸"}
korean_str="�ѱ�"
print(korean_str)
player={"Yuna kim":"skating","Ryu":"baseball","Park":"soccer"}

print("step 1")
print(player)

print("step 2")
print(player.keys())

print("step 3")
print(player.values())

print("step 4")
for player_key in player.keys():
    print(player_key)
    if player_key == 'Ryu':
        print(player['Ryu'])

        break;

    
