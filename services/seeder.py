from manager import *

print(get_players_sorted_by_score())

# #Insere 3 usuários
insert_player('Bjorn', 150)
insert_player('Ragnar', 200)
insert_player('Floki', 300)

#Printa todos os usuários
print(get_players_sorted_by_score())