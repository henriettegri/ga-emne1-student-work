#Kampresultat

def show_match_result(home_team, away_team, home_score, away_score):
    print(f'{home_team}-{away_team}, resultat: {home_score}-{away_score}.')

    if home_score > away_score:
        print('Hjemmeseier!')
    elif home_score < away_score:
        print('Borteseier!')
    else:
        print('Uavgjort!')

show_match_result('Sarpsborg 08', 'Fredrikstad', 5, 2)
show_match_result('Viking', 'Sarpsborg 08', 2, 3)
show_match_result('Rosenborg', 'Sarpsborg 08', 2, 2)