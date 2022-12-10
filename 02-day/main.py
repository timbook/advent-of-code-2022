lines = open('input.txt', 'r').readlines()

opp_to_rps = {'A': 'R', 'B': 'P', 'C': 'S'}
me_to_rps = {'X': 'R', 'Y': 'P', 'Z': 'S'}

choice_to_score = {'R': 1, 'P': 2, 'S': 3}

score = 0

for line in lines:
    opp, me = line.strip().split()
    opp = opp_to_rps[opp]
    me = me_to_rps[me]

    choice_score = choice_to_score[me]

    if opp == me:
        outcome_score = 3

    elif opp == 'R':
        if me == 'P':
            outcome_score = 6
        elif me == 'S':
            outcome_score = 0

    elif opp == 'P':
        if me == 'R':
            outcome_score = 0
        elif me == 'S':
            outcome_score = 6

    elif opp == 'S':
        if me == 'R':
            outcome_score = 6
        elif me == 'P':
            outcome_score = 0

    score += (choice_score + outcome_score)

print(f"A ::: {score}")

opp_to_win = {'R': 'P', 'P': 'S', 'S': 'R'}
opp_to_loss = {'R': 'S', 'P': 'R', 'S': 'P'}

score = 0

for line in lines:
    opp, result = line.strip().split()
    opp = opp_to_rps[opp]

    if result == 'X':
        my_choice = opp_to_loss[opp]
        outcome_score = 0
    elif result == 'Y':
        my_choice = opp
        outcome_score = 3
    elif result == 'Z':
        my_choice = opp_to_win[opp]
        outcome_score = 6

    choice_score = choice_to_score[my_choice]
    
    score += (choice_score + outcome_score)

print(f"B ::: {score}")
