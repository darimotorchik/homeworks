players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

gamer1, gamer2, gamer3 = list(players.items())
new_list = [(*gamer1[0], *gamer1[1]), (*gamer2[0], *gamer2[1]), (*gamer3[0], *gamer3[1])]
print(new_list)
