import random

def numbers_game():
    if reputation >= 2:
        num = random.randint(0,100)
        guess_count = reputation + 6
        global numbers_game_win
        for i  in range(1, guess_count+1):
            guess = int(input("Take a guess... "))
            if guess > num:
                print("This number is too high")
                numbers_game_win = False
                print(f'You have {guess_count - i} attempts left')
            elif guess < num:
                print("This number is too low")
                numbers_game_win = False
                print(f'You have {guess_count - i} attempts left')
            else:
                print("That is correct... You win.")
                numbers_game_win = True
                break
        if numbers_game_win == False:
            print("You lost... I will take some of your reputation HAHAHAHAHAHAHAHAHAHAHA")
    else:
        print(f"The {encounter} doesn't seem to like you very much")
        numbers_game_win = "N/A"





reputation = 4
encounter = "space wizard"
checkpoint2 = True


while checkpoint2: 
    numbers_game()
    if numbers_game_win == True:
        break
    elif numbers_game_win == False:
        reputation -= 1
        print(f"""You start the puzzle again and have lost 1 reputation.
              you now have: {reputation} reputation
              """)
    else:
        print("you go further into the forest")
        break

print("the end")