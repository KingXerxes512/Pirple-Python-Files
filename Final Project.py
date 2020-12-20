# This is a python program that will model the playability of the card game 'Go Fish'

import random as r
from collections import Counter


class Player:
    def __init__(self, Deck: list, Name="NaN"):
        self.Name = Name
        self.Deck = Deck
        self.Books = []

    def __set_name__(self, name):
        self.Name = name

    def __get_name__(self):
        return self.Name

    def setDeck(self, Deck):
        self.Deck = Deck

    def getDeck(self):
        return self.Deck

    def addBook(self, book):
        self.Books.append(book)

    def getBooks(self):
        return self.Books

    def sort(self):
        deck = self.Deck
        deck.sort()
        self.Deck = deck


SUITS = 4
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']
DECK = SUITS * RANKS
Deck1 = []
Deck2 = []

# Create the player decks
while True:
    card = r.choice(DECK)
    Deck1.append(card)
    DECK.remove(card)
    card = r.choice(DECK)
    Deck2.append(card)
    DECK.remove(card)
    if len(DECK) < 39:
        break
Deck1.sort()
Deck2.sort()


# Displays the state of how many books the players have and how many cards are in the stock
def DisplayBoard(Player1, Player2):
    p1 = Player1.__get_name__()
    p1 = p1 + ' Books'
    p2 = Player2.__get_name__()
    p2 = p2 + ' Books'
    print(' Cards in Stock    ', Player1.__get_name__(), ' Books    ', Player2.__get_name__(), ' Books')
    print('----------------  ', '-' * (len(p1) + 3), ' ', '-' * (len(p2) + 3))
    print('      ', len(DECK), '               ', len(Player1.getBooks()), '              ', len(Player2.getBooks()))


def SearchDeckForBooks(Player):
    books = []
    deck_count = Counter(Player.getDeck())
    for key in deck_count:
        if deck_count[key] == 4:
            books.append(key)
    for book in books:
        Player.addBook(book)

    for i in range(4):
        for book in books:
            deck = Player.getDeck()
            deck.remove(book)
            Player.setDeck(deck)


def Request(ReceivingPlayer, GivingPlayer):
    caught = False
    while True:
        print('Your deck: ', ReceivingPlayer.getDeck())
        Card = input('What card would you ask of? ').upper()
        if Card != '--HELP' and Card != 'Q':
            giving_deck_counter = Counter(GivingPlayer.getDeck())
            if Card in giving_deck_counter.keys():
                caught = True
                for i in range(giving_deck_counter[Card]):
                    ReceivingNewDeck = ReceivingPlayer.getDeck()  # Assign the decks for manipulation
                    GivingNewDeck = GivingPlayer.getDeck()
                    ReceivingNewDeck.append(Card)  # Add and remove the card in question
                    GivingNewDeck.remove(Card)
                    ReceivingPlayer.setDeck(ReceivingNewDeck)  # Reassign the altered decks
                    GivingPlayer.setDeck(GivingNewDeck)
            if caught:
                ReceivingPlayer.getDeck().sort()
                GivingPlayer.getDeck().sort()
                print('You caught some cards, you may ask again.')
                return True
            else:
                print('You caught nothing, draw a card')
                if len(DECK) != 0:
                    card = r.choice(DECK)
                    print('You drew a ', card)
                    ReceivingNewDeck = ReceivingPlayer.getDeck()
                    ReceivingNewDeck.append(card)
                    ReceivingNewDeck.sort()
                    ReceivingPlayer.setDeck(ReceivingNewDeck)
                    DECK.remove(card)
                return False
        elif Card == "Q":
            quit()
        else:  # Takes player to the help section
            while True:
                print("""\nInstructions:\n
THE PACK
The standard 52-card pack is used. Some cards will be dealt and the rest will form the stock pile.

OBJECT OF THE GAME
The goal is to win the most "books" of cards. A book is any four of a kind, such as four kings, four aces, and so on.

RANK OF CARDS
The cards rank from ace (high) to two (low). The suits are not important, only the card numbers are relevant, such as
two 3s, two 10s, and so on.

THE DEAL
Any player deals one card face up to each player. The player with the lowest card is the dealer. The dealer shuffles 
the cards, and the player to the right cuts them.The dealer completes the cut and deals the cards clockwise one at a 
time, face down, beginning with the player to the left. If two or three people are playing, each player receives seven 
cards. If four or five people are playing, each receives five cards. The remainder of the pack is placed face down on 
the table to form the stock.

THE PLAY
The player to the left of the dealer looks directly at any opponent and says, for example, "Give me your kings," 
usually addressing the opponent by name and specifying the rank that they want, from ace down to two. The player who 
is "fishing “must have at least one card of the rank that was asked for in their hand. The player who is addressed must 
hand over all the cards requested. If the player has none, they say, "Go fish!" and the player who made the request 
draws the top card of the stock and places it in their hand. If a player gets one or more cards of the named rank that 
was asked for, they are entitled to ask the same or another player for a card. The player can ask for the same card or 
a different one. So long as the player succeeds in getting cards (makes a catch), their turn continues. When a player 
makes a catch, they must reveal the card so that the catch is verified. If a player gets the fourth card of a book, 
the player shows all four cards, places them on the table face up in front of everyone, and plays again.
If the player goes fishing without "making a catch" (does not receive a card he asked for), the turn passes to the left.
The game ends when all thirteen books have been won. The winner is the player with the most books. During the game, if 
a player is left without cards, they may (when it's their turn to play), draw from the stock and then ask for cards of 
that rank. If there are no cards left in the stock, they are out of the game.\n""")
                x = input("Enter '--resume' to resume: ")
                if x == '--resume':
                    repeatNeeded = True
                    break


def HasPlayerWon(Player1, Player2):
    if Player1.getBooks() + Player2.getBooks() == 13:  # If all books have been acquired the game is over
        if len(Player1.getBooks()) > len(Player2.getBooks()):
            return Player1
        else:
            return Player2
    elif Player1.getDeck == [] and DECK == []:  # If someone has no cards and there is no stock, the game is over
        return Player1
    elif Player2.getDeck == [] and DECK == []:
        return Player2
    else:
        return False


PlayerWon = False
Player1 = Player(Deck1, input("Please enter your name, Player 1: "))
Player2 = Player(Deck2, input("Please enter your name, Player 2: "))
# Game Loop
while True:
    DisplayBoard(Player1, Player2)
    print(Player1.__get_name__() + "'s turn!")
    while Request(Player1, Player2):
        pass
    SearchDeckForBooks(Player1)
    PlayerWon = HasPlayerWon(Player1, Player2)
    if PlayerWon == Player1:
        print(Player1.__get_name__(), ' has won!')
        break
    elif PlayerWon == Player2:
        print(Player2.__get_name__(), ' has won!')
        break
    else:
        pass

    DisplayBoard(Player1, Player2)
    print(Player2.__get_name__() + "'s turn!")
    while Request(Player2, Player1):
        pass
    SearchDeckForBooks(Player2)
    if PlayerWon == Player1:
        print(Player1.__get_name__(), ' has won!')
        break
    elif PlayerWon == Player2:
        print(Player2.__get_name__(), ' has won!')
        break
    else:
        pass
