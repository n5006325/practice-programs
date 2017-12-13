# Filename : rock_paper_scirssors.py

# two player rock-paper-scissors game
# print out congrats to the winner
# ask if want to start a new game



running = True

while running:
    playGame = input('Do you want to play Rock, paper, scissors (Y/N)?: ')
    if playGame == 'y' or 'Y':
        player1 = input("Player 1 - Rock, paper, scissors: ")
        player2 = input("Player 2 - Rock, paper, scissors: ")

        if player1 == "rock" and player2 == 'scissors':
            print('Player 1 wins', player1, 'beats', player2)
        elif player1 == "scissors" and player2 == 'paper':
            print('Player 1 wins', player1, 'beats', player2)
        elif player1 == 'paper' and player2 == 'rock':
            print('Player 1 wins', player1, 'beats', player2)
        else:
            print('Player2 wins', player2, 'beats', player1)
    else:
        running = False
print('Thanks for playing')
