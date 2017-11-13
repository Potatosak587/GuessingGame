import random
import time

'''
Turtles List:

    a - represents Player One in Multiplayer Versus or the Human Player in Single Player/Player vs. Computer
    b - represents Player Two in Multiplayer Versus or the Computer in Player vs. Computer
    m - handles the menu and user interfaces
    n - handles the 'confused' messages

'''

def dumb_guess(max_range):
    random_guess = random.randrange(1,max_range)
    return random_guess

def smart_guess(guess_low, guess_high):
    educated_guess = random.randrange(guess_low,guess_high + 1)
    return educated_guess

def computer_round(max_range,computer_strength):
    playing = True
    while playing == True:
        random_number = random.randrange(1, max_range)

        print("Starting Computer Round:")
        print(" ")
        print("Random number is:")
        print(random_number)

        turn_counter = 0

        guess_low = 1
        guess_high = max_range

        while playing == True:
            turn_counter = turn_counter + 1

            print("Turn #:")
            print(turn_counter)
            print(" ")

            time.sleep(1)

            if computer_strength == 1:
                computer_guess = dumb_guess(max_range)
            elif computer_strength == 2:
                computer_guess = smart_guess(guess_low,guess_high)

            print("The Computer's Guess:")
            print(computer_guess)
            print(" ")

            time.sleep(1)

            if computer_guess > random_number:
                print("The Computer's guess is too high!")
                # If the computer's guess is too high, the most it will
                #    guess afterwards is the high guess - 1.
                guess_high = computer_guess - 1
            elif computer_guess < random_number:
                print("The Computer's guess is too low!")
                # If the computer's guess is too low, the least it will
                #    guess afterwards is the low guess + 1.
                guess_low = computer_guess + 1
            elif computer_guess == random_number:
                print("The computer's guess is correct!")
                return turn_counter

            time.sleep(1)


def game_round(max_range):
    playing = True
    while playing == True:
        random_number = random.randrange(1, max_range)

        print("Remember that you can quit at any time by entering 0. ")
        print(" ")
        print("Starting Round:")
        print(" ")
        print("Random number is:")
        print(random_number)

        time.sleep(2)

        turn_counter = 0

        while playing == True:
            turn_counter = turn_counter + 1

            print("Turn #:")
            print(turn_counter)
            print(" ")

            time.sleep(1)

            human_guess = ask_guess(max_range)
            if human_guess == 0:
                return 0
            if human_guess > random_number:
                print("Your guess is too high!")
            elif human_guess < random_number:
                print("Your guess is too low!")
            elif human_guess == random_number:
                print("Your guess is correct, congratulations!")
                return turn_counter

            print(" ")

            time.sleep(1)

def game_sp():
    # Single Player Mode
    # Range is determined by the difficulty() function, which returns
    #   the max range of the guessing game

    print("Playing Single Player")
    print(" ")
    print("    Guess a number in the range given, and the program")
    print("    will tell you whether your guess is too high or low.")
    print("------------------------------------------")

    difficulty_num = difficulty()
    if difficulty_num == 0:
        return 2
    else:
        max_range = difficulty_num + 1

    playing = True
    while playing:
        round_result = game_round(max_range)

        if round_result == 0:
            print("Game ended, what would you like to do?")
        else:
            print("Number of Guesses This Round:")
            print(round_result)
            print("What would you like to do?")
        print(" ")
        print("    1. Play again.")
        print("    2. Return to Main Menu.")
        print("    0. Quit Guessing Game.")
        print("------------------------------------------")
        playing_again = [1, 2, 0]
        playing_again_confirm = ask(playing_again)
        if playing_again_confirm == 0:
            return 0
        elif playing_again_confirm == 2:
            return 2

def game_pvp():
    # Multiplayer Versus Mode
    # Range is determined by the difficulty() function, which returns
    #   the max range of the guessing game

    print("Playing Multi Player Versus")
    print(" ")
    print("    Take turns completing rounds of the Guessing Game.")
    print("    The player with the least guesses wins a point, and")
    print("    first player to three wins takes all.")
    print("------------------------------------------")

    difficulty_num = difficulty()
    if difficulty_num == 0:
        return 2
    else:
        max_range = difficulty_num + 1

    player_1 = 0
    player_1_score = 0

    player_2 = 0
    player_2_score = 0

    playing = True
    while playing:
        while player_1 < 3 and player_2 < 3:

            # Run Player One's turn
            print("Player One's Turn:")

            player_1_score = game_round(max_range)
            if player_1_score == 0:
                break
            else:
                print("Player One's Number of Guesses This Round:")
                print(player_1_score)
            print("------------------------------------------")

            # Run Player Two's turn
            print("Player Two's Turn:")

            player_2_score = game_round(max_range)
            if player_2_score == 0:
                break
            else:
                print("Player Two's Number of Guesses This Round:")
                print(player_2_score)
            print("------------------------------------------")

            time.sleep(2)

            # Compare number of guesses for each player, and award a point to the player with
            #    the least guesses.
            # A tie means no points are given.
            if player_1_score < player_2_score:
                print("Player 1 wins this round!")
                player_1 = player_1 + 1
            elif player_2_score < player_1_score:
                print("Player 2 wins this round!")
                player_2 = player_2 + 1
            elif player_1_score == player_2_score:
                print("There was a tie! No change in points.")

            time.sleep(2)

            print(" ")
            print("Scores:")
            print(" ")
            print("Player 1:")
            print(player_1)
            print("Player 2:")
            print(player_2)
            print(" ")

            if player_1 == 3:
                print("Player One wins the game!")
            elif player_2 == 3:
                print("Player Two wins the game!")
            print("------------------------------------------")

        time.sleep(2)

        print("Game ended, what would you like to do?")
        print(" ")
        print("    1. Play again.")
        print("    2. Return to Main Menu.")
        print(" ")
        print("    0. Quit Guessing Game.")
        print("------------------------------------------")

        playing_again = [1, 2, 0]
        playing_again_confirm = ask(playing_again)
        if playing_again_confirm == 0:
            return 0
        elif playing_again_confirm == 2:
            return 2

def game_pve():
    # Player vs. Computer Mode
    # Range is determined by the difficulty() function, which returns
    #   the max range of the guessing game
    # Strength of A.I. is determined by the AI() function
        # The Easy AI guesses completely randomly
        # The Smart AI guesses based between its previous guesses

    print("Playing Player vs. Computer Mode")
    print(" ")
    print("    Take turns completing rounds against a Computer.")
    print("    The player with the least guesses wins a point, and")
    print("    first player to three wins takes all.")
    print("------------------------------------------")

    difficulty_num = difficulty()
    if difficulty_num == 0:
        return 2
    else:
        max_range = difficulty_num + 1

    computer_strength = difficulty_comp()
    if computer_strength == 0:
        return 2

    player_1 = 0
    player_1_score = 0

    computer = 0
    computer_score = 0

    playing = True
    while playing:
        while player_1 < 3 and computer < 3:

            # Run Player One's turn
            print("Player One's Turn:")

            player_1_score = game_round(max_range)
            if player_1_score == 0:
                break
            else:
                print("Player One's Number of Guesses This Round:")
                print(player_1_score)
            print("------------------------------------------")

            # Run Computer's turn
            print("Computer's Turn:")

            computer_score = computer_round(max_range,computer_strength)
            if computer_score == 0:
                break
            else:
                print("Computer's Number of Guesses This Round:")
                print(computer_score)
            print("------------------------------------------")

            time.sleep(2)

            # Compare number of guesses for each player, and award a point to the player with
            #    the least guesses.
            # A tie means no points are given.
            if player_1_score < computer_score:
                print("Player 1 wins this round!")
                player_1 = player_1 + 1
            elif computer_score < player_1_score:
                print("Computer wins this round!")
                computer = computer + 1
            elif player_1_score == computer_score:
                print("There was a tie! No change in points.")

            time.sleep(2)

            print(" ")
            print("Scores:")
            print(" ")
            print("Player 1:")
            print(player_1)
            print("Computer:")
            print(computer)
            print(" ")

            if player_1 == 3:
                print("Player One wins the game!")
            elif computer == 3:
                print("Computer wins the game!")
            print("------------------------------------------")

        time.sleep(2)

        print("Game ended, what would you like to do?")
        print(" ")
        print("    1. Play again.")
        print("    2. Return to Main Menu.")
        print(" ")
        print("    0. Quit Guessing Game.")
        print("------------------------------------------")

        playing_again = [1, 2, 0]
        playing_again_confirm = ask(playing_again)
        if playing_again_confirm == 0:
            return 0
        elif playing_again_confirm == 2:
            return 2

def game_pvp_bet():
    # Multiplayer Versus Mode
    # Range is determined by the difficulty() function, which returns
    #   the max range of the guessing game
    # Players bet on rounds, and the person with the least guesses wins the pot.
    # First player to $150 or more wins

    print("Playing Multi Player Versus - Betting")
    print(" ")
    print("    Take turns completing rounds of the Guessing Game.")
    print("    Both sides start with 100 points, and each bet on a")
    print("    round of the Guessing Game.")
    print("    The player with the least guesses wins the pot, and")
    print("    first player to 150 points wins.")
    print("------------------------------------------")

    difficulty_num = difficulty()
    if difficulty_num == 0:
        return 2
    else:
        max_range = difficulty_num + 1

    player_1 = 0
    player_1_score = 0

    player_2 = 0
    player_2_score = 0

    playing = True
    while playing:
        while player_1 < 3 and player_2 < 3:

            # Program asks for bet for the round
            # Bet placed cannot exceed the points given to each player

            print("Place a bet for this Round.")
            print(" ")
            print("The bet placed cannot be more than what either")
            print("    player owns.")

            if player_1 >= player_2:
                bet = ask_guess(player_2)
            elif player_1 < player_2:
                bet = ask_guess(player_1)

            # Run Player One's turn
            print("Player One's Turn:")

            player_1_score = game_round(max_range)
            if player_1_score == 0:
                break
            else:
                print("Player One's Number of Guesses This Round:")
                print(player_1_score)
            print("------------------------------------------")

            # Run Player Two's turn
            print("Player Two's Turn:")

            player_2_score = game_round(max_range)
            if player_2_score == 0:
                break
            else:
                print("Player Two's Number of Guesses This Round:")
                print(player_2_score)
            print("------------------------------------------")

            time.sleep(2)

            # Compare number of guesses for each player, and award a point to the player with
            #    the least guesses.
            # A tie means no points are given.
            if player_1_score < player_2_score:
                print("Player 1 wins this round!")
                player_1 = player_1 + bet
                player_2 = player_2 - bet
            elif player_2_score < player_1_score:
                print("Player 2 wins this round!")
                player_2 = player_2 + bet
                player_1 = player_1 - bet
            elif player_1_score == player_2_score:
                print("There was a tie! No change in points.")

            time.sleep(2)

            print(" ")
            print("Bet from this round:")
            print(bet)

            print(" ")
            print("Scores:")
            print(" ")
            print("Player 1:")
            print(player_1)
            print("Player 2:")
            print(player_2)
            print(" ")

            if player_1 == 3:
                print("Player One wins the game!")
            elif player_2 == 3:
                print("Player Two wins the game!")
            print("------------------------------------------")

        time.sleep(2)

        print("Game ended, what would you like to do?")
        print(" ")
        print("    1. Play again.")
        print("    2. Return to Main Menu.")
        print(" ")
        print("    0. Quit Guessing Game.")
        print("------------------------------------------")

        playing_again = [1, 2, 0]
        playing_again_confirm = ask(playing_again)
        if playing_again_confirm == 0:
            return 0
        elif playing_again_confirm == 2:
            return 2

def game_pve_bet():
    # Player vs. Computer Mode - betting
    # Range is determined by the difficulty() function, which returns
    #   the max range of the guessing game
    # Strength of A.I. is determined by the AI() function
    # The Easy AI guesses completely randomly
    # The Smart AI guesses based between its previous guesses
    # Players bet on rounds, and the person with the least guesses wins the pot.
    # First player to $150 or more wins

    print("Playing Player vs. Computer - Betting")
    print(" ")
    print("    Take turns completing rounds against a Computer.")
    print("    Both sides start with 100 points, and each bet on a")
    print("    round of the Guessing Game.")
    print("    The player with the least guesses wins the pot, and")
    print("    first player to 150 points wins.")
    print("------------------------------------------")

    difficulty_num = difficulty()
    if difficulty_num == 0:
        return 2
    else:
        max_range = difficulty_num + 1

    computer_strength = difficulty_comp()
    if computer_strength == 0:
        return 2

    player_1 = 100
    player_1_score = 0

    computer = 100
    computer_score = 0

    print("Starting Scores:")
    print(" ")
    print("Player 1:")
    print(player_1)
    print("Computer:")
    print(computer)

    playing = True
    while playing:
        while player_1 < 150 and computer < 150:

            # Program asks for bet for the round
            # Bet placed cannot exceed the points given to each player

            print("Place a bet for this Round.")
            print(" ")
            print("The bet placed cannot be more than what either")
            print("    player owns.")

            if player_1 >= computer:
                bet = ask_guess(computer)
            elif player_1 < computer:
                bet = ask_guess(player_1)

            # Run Player One's turn
            print("Player One's Turn:")

            player_1_score = game_round(max_range)
            if player_1_score == 0:
                break
            else:
                print("Player One's Number of Guesses This Round:")
                print(player_1_score)
            print("------------------------------------------")

            # Run Computer's turn
            print("Computer's Turn:")

            computer_score = computer_round(max_range, computer_strength)
            if computer_score == 0:
                break
            else:
                print("Computer's Number of Guesses This Round:")
                print(computer_score)
            print("------------------------------------------")

            time.sleep(2)

            # Compare number of guesses for each player, and award a point to the player with
            #    the least guesses.
            # A tie means no points are given.
            if player_1_score < computer_score:
                print("Player 1 wins this round!")
                player_1 = player_1 + bet
                computer = computer - bet
            elif computer_score < player_1_score:
                print("Computer wins this round!")
                computer = computer + bet
                player_1 = player_1 - bet
            elif player_1_score == computer_score:
                print("There was a tie! No change in points.")

            time.sleep(2)

            print(" ")
            print("Bet from this round:")
            print(bet)

            print(" ")
            print("Scores:")
            print(" ")
            print("Player 1:")
            print(player_1)
            print("Computer:")
            print(computer)
            print(" ")

            if player_1 >= 150:
                print("Player One wins the game!")
            elif computer >= 150:
                print("Computer wins the game!")
            print("------------------------------------------")

        time.sleep(2)

        print("Game ended, what would you like to do?")
        print(" ")
        print("    1. Play again.")
        print("    2. Return to Main Menu.")
        print(" ")
        print("    0. Quit Guessing Game.")
        print("------------------------------------------")

        playing_again = [1, 2, 0]
        playing_again_confirm = ask(playing_again)
        if playing_again_confirm == 0:
            return 0
        elif playing_again_confirm == 2:
            return 2

def difficulty():
    # Difficulties are 1: Easy, 2: Normal, 3: Hard
    # This function asks for a difficulty, and returns the max value of
    #   the guessing game's range back.

    print("Select a Game Difficulty:")
    print(" ")
    print("    1. Easy - Number is between 1 and 10")
    print("    2. Normal - Number is between 1 and 20")
    print("    3. Hard - Number is between 1 and 100")
    print(" ")
    print("    0. Return to Main Menu")
    print("------------------------------------------")

    asking_list = [1, 2, 3, 0]
    game_difficulty = ask(asking_list)

    if game_difficulty == 1:
        print("Selecting Easy Difficulty")
        print("------------------------------------------")
        return 10
    elif game_difficulty == 2:
        print("Selecting Normal Difficulty")
        print("------------------------------------------")
        return 20
    elif game_difficulty == 3:
        print("Selecting Hard Difficulty")
        print("------------------------------------------")
        return 100
    elif game_difficulty == 0:
        return 0

def difficulty_comp():
    # Difficulties are 1: Easy, 2: Hard
    # This function asks for a difficulty, and returns the value of
    #   the computer's AI back.

    print("Select a Computer AI Difficulty:")
    print(" ")
    print("    1. Easy - The Computer guesses randomly every turn")
    print("    2. Hard - The Computer guesses based on its previous guesses")
    print(" ")
    print("    0. Return to Main Menu")
    print("------------------------------------------")

    asking_list = [1, 2, 0]
    game_difficulty = ask(asking_list)

    if game_difficulty == 1:
        print("Selecting Easy Computer")
        print("------------------------------------------")
        return 1
    elif game_difficulty == 2:
        print("Selecting Hard Computer")
        print("------------------------------------------")
        return 2
    elif game_difficulty == 0:
        return 0


def ask(asking_list):
    # This is my basic function for user inputs
    # It needs a list of answers, and if the input given is not in the list,
    #     the program asks for another input.
    asking = True
    while asking == True:
        response = input("Ready for a response!")
        print(" ")
        if response in asking_list:

            return response
        else:
            print("Sorry, I didn't understand that.")

def ask_guess(max_range):
    # This is the function for asking for guesses and/or bets during the actual game
    # Range is based on the difficulty selected
    asking = True
    while asking == True:
        response = input("What do you want to input?")
        print(" ")
        if 0 <= response <= max_range:

            return response
        else:
            print("Sorry, that isn't a legitimate response.")

def run_game():

    asking_list = [1,2,3,4,5,0]

    playing = True
    while playing:
        print("------------------------------------------")
        print("Welcome to the Guessing Game! - Kyle Yen")
        print("What mode would you like to play?")
        print(" ")
        print("    1. Single Player Mode")
        print("        - Play a casual round by yourself.")
        print(" ")
        print("    2. Multi Player Versus Mode")
        print("        - Play a head-to-head round with a friend!")
        print("          First to three victories wins.")
        print(" ")
        print("    3. Player vs. Computer Mode")
        print("        - Play a round against a Computer AI.")
        print("          First to three victories wins.")
        print(" ")
        print("    4. Multi Player Versus Mode - Betting")
        print("        - Play a head-to-head round with a friend!")
        print("          Start with 100 points, and bet.")
        print("          First to 150 points wins.")
        print(" ")
        print("    5. Player vs. Computer Mode - Betting")
        print("        - Play a round against a Computer AI.")
        print("          Start with 100 points, and bet.")
        print("          First to 150 points wins.")
        print(" ")
        print("    0. Quit game")
        print("------------------------------------------")

        input = ask(asking_list)

        output = 0

        if input == 1:
            # Run single player mode
            output = game_sp()
        elif input == 2:
            # Run multi player vs. mode
            output = game_pvp()
        elif input == 3:
            # Run player vs. computer mode
            output = game_pve()
        elif input == 4:
            # Run multi player vs. mode - betting
            output = game_pvp_bet()
        elif input == 5:
            # Run player vs. computer mode - betting
            output = game_pve_bet()
        elif input == 0:
            # Quit game
            print("Quitting game.")
            print("------------------------------------------")
            return 0
        if output == 0:
            print("Quitting game.")
            print("------------------------------------------")
            return 0

def main():

    run_game()

main()