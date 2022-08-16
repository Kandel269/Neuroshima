

def army_win_ratio(duels,armies):
    list_score_2D_armies = []
    armies_list = []

    for army in armies:
        armies_list.append(str(army))
        army_score_list = []
        army_score_list.append(army.name)
        for _ in range(len(armies)):
            army_score_list.append(0)
        list_score_2D_armies.append(army_score_list)

    for duel in duels:
        player_1 = ""
        army_1_index = 0
        player_2 = ""
        army_2_index = 0

        lock = 0
        winner = str(duel.winner)
        for player in duel.users.all():
            if lock == 0:
                army_1 = str(player.army)
                army_1_index = armies_list.index(army_1)
                player_1 = str(player.user.username)
                lock += 1
            army_2 = str(player.army)
            army_2_index = armies_list.index(army_2)
            player_2 = str(player.user.username)

        if winner == player_1:
            list_score_2D_armies[army_1_index][army_2_index + 1] += 1
        elif winner == player_2:
            list_score_2D_armies[army_2_index][army_1_index + 1] += 1

    list_score_win_ratio = []

    for army_score in range(len(list_score_2D_armies)):
        lock = 0
        army_win_ratio = []
        for score in range(len(list_score_2D_armies[army_score])):
            if lock == 0:
                army_win_ratio.append(list_score_2D_armies[army_score][score])
                lock += 1
                continue

            if list_score_2D_armies[army_score][score] == 0:
                army_win_ratio.append("0%")
            else:
                if int(list_score_2D_armies[score-1][army_score+1]) == 0:
                    army_win_ratio.append("100%")
                else:
                    army_win_ratio.append(str(round((
                        int(list_score_2D_armies[army_score][score])
                        /
                        ((list_score_2D_armies[army_score][score])+int(list_score_2D_armies[score-1][army_score+1]))
                    )*100,2))
                    +"%")


        list_score_win_ratio.append(army_win_ratio)

    return list_score_win_ratio