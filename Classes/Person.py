class Person:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # Function that removes a card from the person's deck
    def remove_one(self):
        return self.all_cards.pop(0)

    # Function that adds new card(s) in to the deck
    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    # Print function
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

    # Function that returns the length of the deck
    def __len__(self):
        return len(self.all_cards)
