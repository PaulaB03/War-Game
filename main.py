from Classes.Deck import Deck
from Classes.Person import Person

import os
# Function to clear the historical output
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to stop the game
def stop_game():
    choice = 'wrong'

    while choice not in ['Y', 'y', 'n', 'N']:
        choice = input("Would you like to continue the game? Y or N ")

        # Checks if the input is valid
        if choice not in ['Y', 'y', 'n', 'N']:
            print("Sorry, I didn't understand.")

    if choice in ['Y', 'y']: return True
    else:                    return False

# Creates the 2 players
clear()
player_one = Person(input("Player one name: "))
player_two = Person(input("Player two name: "))

# Creates the card deck then shuffles it
card_deck = Deck()
card_deck.shuffle()

# Split the deck between players
for x in range(int(len(card_deck)/2)):
    player_one.add_cards(card_deck.deal_one())
    player_two.add_cards(card_deck.deal_one())

del card_deck

# The actual game
game_on = True
# Variable to keep track of the game
round_num = 0

# Game Starts
while game_on:
    clear()

    round_num += 1
    print(f'Round {round_num}')

    # Check to see if a player is out of cards
    if len(player_one) == 0:
        clear()
        print(f'{player_one.name} is out of cards! Game Over')
        print(f'{player_two.name} Wins after {round_num} rounds')
        break

    if len(player_two) == 0:
        clear()
        print(f'{player_two.name} is out of cards! Game Over')
        print(f'{player_one.name} Wins after {round_num} rounds')
        break

    # Reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # Start a new round
    at_war = True
    while at_war:
        print(f'    {player_one.name} was {player_one_cards[-1]}')
        print(f'    {player_two.name} was {player_two_cards[-1]}')

        # If Player One wins the round
        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets all the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            # No longer at 'war' and the round is finished
            print(f'\n{player_one.name} won the round.\n')
            at_war = False

        # If Player Two wins the round
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets all the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            # No longer at 'war' and the round is finished
            print(f'\n{player_one.name} won the round.\n')
            at_war = False

        # If it's a draw
        else:
            print("\nIT'S WAR!")

            # Check to see if a player is out of cards
            if len(player_one) < 5:
                print(f'{player_one.name} has {len(player_one)} card(s) and can not play war! Game Over at War')
                print(f'{player_two.name} Wins!')
                game_on = False
                break

            elif len(player_two) < 5:
                print(f'{player_two.name} has {len(player_two)} card(s) and can not play war! Game Over at War')
                print(f'{player_one.name} Wins!')
                game_on = False
                break

            # Otherwise each player will draw cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

    print(f'{player_one.name} has {len(player_one)} card(s)')
    print(f'{player_two.name} has {len(player_two)} card(s)\n')
    game_on = stop_game()

    # If the user quits the game display final info
    if not game_on:
        clear()
        print("The game has been stopped.")
        print(f'{player_one.name} had {len(player_one)} card(s)')
        print(f'{player_two.name} had {len(player_two)} card(s)')
