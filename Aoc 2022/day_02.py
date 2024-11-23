# part one
with open('input02.txt','r') as f:
    data = [x.split() for x in f.read().split('\n')][:-1]

points = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
score = 0

for game in data:
    score_elf = points[game[0]]
    score_player = points[game[1]]

    score += score_player

    if score_elf == score_player:
        score += 3
    elif score_elf > score_player and abs(score_player - score_elf) == 1 or (score_elf == 1 and score_player == 3):
        score += 0
    else:
        score += 6
    
# part two
points = {'X': 0, 'Y': 3, 'Z': 6}
win = {'A': 2, 'B': 3, 'C': 1} # a = rock so we need paper (2), B = paper, need scissors (3) ...
draw = {'A': 1, 'B': 2, 'C': 3}
loss = {'A': 3, 'B': 1, 'C': 2}
score = 0
for game in data:
    preferred_outcome = points[game[1]]
    score += preferred_outcome

    if preferred_outcome == 0:
        score += loss[game[0]]
    elif preferred_outcome == 3:
        score += draw[game[0]]
    else:
        score += win[game[0]]

print(score)
