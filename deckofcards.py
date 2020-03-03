class Card():
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
        names = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }
        self.name = names.get(value) or str(value)

    def show_value(self):
        print(f"{self.name} of {self.suit}")


ace_of_hearts = Card('hearts', 2)
ace_of_hearts.show_value()


class Deck():
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for value in range(1, 14):

                self.cards.append(Card(suit, value))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def sort(self):
        Hearts = []
        Clubs = []
        Diamonds = []
        Spades = []
        for i in range(len(self.cards)):
            if self.cards[i].suit == "Hearts":
                Hearts.append(self.cards[i].value)

            elif self.cards[i].suit == "Clubs":
                Clubs.append(self.cards[i].value)

            elif self.cards[i].suit == "Diamonds":
                Diamonds.append(self.cards[i].value)

            elif self.cards[i].suit == "Spades":
                Spades.append(self.cards[i].value)

        # here is where we order the values from least to greatest

        print(Hearts)
        print(Clubs)
        print(Diamonds)
        print(Spades)

    def game(self):
        pass


bicycle_deck = Deck()

bicycle_deck.shuffle()

bicycle_deck.sort()

for card in bicycle_deck.cards:
    card.show_value()
