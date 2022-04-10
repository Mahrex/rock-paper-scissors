import random
import art
import os
import art_2

while True:

    # Initializing the game
    print(art_2.main_art)
    print('------------------------------------')
    print('Welcome to Rock-Paper-Scissors game!\n\n')
    print('GAME RULES:-')
    print("Press '1' for ROCK\nPress '2' for PAPER\nPress '3' for SCISSORS")
    print('\nThe game will be played between User and Computer, whoever scores 5 first will win the game!')

    # Scores of the players
    player_score = 0
    computer_score = 0
    round_num = 1

    # GAME-ON
    game_on = True

    # Starting of the main game
    while game_on:
        
        # Choices of players!
        print(f'\nRound: {round_num}')
        round_num += 1
        player_choice = int(input('Enter your choice: '))
        print()
        computer_choice = random.randint(1,3)
        
        # Draw between Computer and User!
        if player_choice == 1 and computer_choice == 1:
            print('Player chooses ROCK')
            print(art.hand[0])
            print('Computer chooses ROCK')
            print(art.hand[0])
            print('This round is a draw!')
            
        elif player_choice == 2 and computer_choice == 2:
            print('Player chooses PAPER')
            print(art.hand[1])
            print('Computer chooses PAPER')
            print(art.hand[1])
            print('This round is a draw!')
            
        elif player_choice == 3 and computer_choice == 3:
            print('Player chooses SCISSORS')
            print(art.hand[2])
            print('Computer chooses SCISSORS')
            print(art.hand[2])
            print('This round is a draw!') 
            
        # Win situations! (USER)
        elif player_choice == 1 and computer_choice == 3:
            player_score += 1
            print('Player chooses ROCK')
            print(art.hand[0])
            print('Computer chooses SCISSORS')
            print(art.hand[2])
            print('USER won this round!')
            print(f'SCORES:-\nUser = {player_score}\nComputer = {computer_score}\n')
            
        elif player_choice == 2 and computer_choice == 1:
            player_score += 1
            print('Player chooses PAPER')
            print(art.hand[1])
            print('Computer chooses ROCK')
            print(art.hand[0])
            print('USER won this round!')
            print(f'SCORES:-\nUser = {player_score}\nComputer = {computer_score}\n')
            
        elif player_choice == 3 and computer_choice == 2:
            player_score += 1
            print('Player chooses SCISSORS')
            print(art.hand[2])
            print('Computer chooses PAPER')
            print(art.hand[1])
            print('USER won this round!')
            print(f'SCORES:-\nUser = {player_score}\nComputer = {computer_score}\n')
            
        # (COMPUTER)
        elif player_choice == 3 and computer_choice == 1:
            computer_score += 1
            print('Player chooses SCISSORS')
            print(art.hand[2])
            print('Computer chooses ROCK')
            print(art.hand[0])
            print('COMPUTER won this round!')
            print(f'SCORES:-\nUser = {player_score}\nComputer = {computer_score}\n')
            
        elif player_choice == 1 and computer_choice == 2:
            computer_score += 1
            print('Player chooses ROCK')
            print(art.hand[0])
            print('Computer chooses PAPER')
            print(art.hand[1])
            print('COMPUTER won this round!')
            print(f'SCORES:-\nUser = {player_score}\nComputer = {computer_score}\n')
            
        elif player_choice == 2 and computer_choice == 3:
            computer_score += 1
            print('Player chooses PAPER')
            print(art.hand[1])
            print('Computer chooses SCISSORS')
            print(art.hand[2])
            print('COMPUTER won this round!')
            print(f'SCORES:-\nUser = {player_score}\nComputer = {computer_score}\n')
            
        # Checking that if anyone won the game or not 
        if player_score == 5:
            print('\nCongratulations! You won the game! 🍻\n')
            game_on = False
        if computer_score == 5:
            print('\nSorry, you lost! 😓\n')
            game_on = False
            
            
    # Play again!
    play_again = input('Want to play again? (Y/N): ')
    
    if play_again[0].upper() == 'Y':
        os.system('cls')
        continue
    elif play_again[0].upper() == 'N':
        print('\nThanks for playing the game!\n')
        break
    else:
        print('\nInvalid input, exiting game.\n')
        break