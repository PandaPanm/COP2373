import random


class Card:
    """Represents a single playing card."""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents a deck of 52 playing cards."""

    def __init__(self):
        self.cards = []
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self._create_deck()

    def _create_deck(self):
        """Create a deck of 52 cards."""
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def deal(self, num_cards):
        """Deals a specified number of cards."""
        return [self.cards.pop() for _ in range(num_cards)]


def display_hand(hand):
    """Display the current hand of cards."""
    for i, card in enumerate(hand, 1):
        print(f"{i}. {card}")


def main():
    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Deal the initial 5-card hand
    hand = deck.deal(5)
    print("Your initial Poker hand:")
    display_hand(hand)

    # Prompt the user for card replacement choices
    replace = input("Enter the numbers (separated by commas) of the cards you want to replace (e.g., 1, 3, 5): ")
    replace_indices = [int(x.strip()) - 1 for x in replace.split(",") if x.strip().isdigit()]

    # Replace the chosen cards
    for index in replace_indices:
        if 0 <= index < len(hand):
            hand[index] = deck.deal(1)[0]  # Replace the card with a new card from the deck

    print("\nYour hand after the draw:")
    display_hand(hand)


if __name__ == "__main__":
    main()
