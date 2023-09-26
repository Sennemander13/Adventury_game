import random

betted_item = input("choose an item to bet...")
wincon = 0
Pscore = 0
Bscore = 0

while wincon < 3:
    choices = [1, 2, 3]
    outcome = random.choice(choices)
    print("rock, paper, scissor shoot!")
    Pchoice = int(input("""Enter:
                             1 : rock
                             2 : paper
                             3 : scissor
                    """))
    if (Pchoice == 2 and outcome == 1) or (Pchoice == 1 and outcome == 3) or (Pchoice == 3 and outcome == 2):
        print("You won this round")
        wincon += 1
        Pscore += 1
    elif (Pchoice == 1 and outcome == 2) or (Pchoice == 3 and outcome == 1) or (Pchoice == 2 and outcome == 3):
        print("haha I won this round")
        wincon += 1
        Bscore += 1
    else:
        print("a draw... let's try again")
    print(f'the score is {Pscore} - {Bscore}')

if Pscore > Bscore:
    print("damn I lost... you can now venture into the dungeon")
else:
    print(f"I already knew you couldn't beat me HAHAHAHAHAHA. I will take your {betted_item} now")