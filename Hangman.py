from random import randint


def ClearTerminal():
    for i in range(50):
        print('')


def SelectMode():
    while True:
        print('Would you like to play against a computer or enter two player mode?')
        mode = int(input('Please enter the number 1 or 2 for the number of players. '))
        if mode != 1 and mode != 2:
            ClearTerminal()
            print('That is an invalid response.')
        else:
            if mode == 1:
                mode = 'SINGLE-PLAYER'
            else:
                mode = 'TWO-PLAYER'
            return mode


mode = SelectMode()


HANGMAN_PICS = ['''
      +---+
          |
          |
          |
         ===''', '''
      +---+
      O   |
          |
          |
         ===''', '''
      +---+
      O   |
      |   |
          |
         ===''', '''
      +---+
      O   |
     /|   |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
     /    |
         ===''', '''
      +---+
      O   |
     /|\  |
     / \  |
         ===''']

alreadyGuessed = []  # Will hold already guessed characters
missedLetters = []  # Will contain the letters guessed that are not in the word
correctLetters = []  # Will contain the letters guessed that are in the word


def getWord():
    WORD_LIST = open('Words.txt', 'rt')
    Words = []
    for line in WORD_LIST:
        Words.append(line)
    WORD_LIST.close()
    return Words[randint(0, len(Words))]


if mode == 'SINGLE-PLAYER':
    Game_Word = getWord()
else:
    Game_Word = input('Enter the secret word for you match. ').lower()


def getGuess():
    while True:
        player_guess = input('Guess a letter. ').lower()
        if len(player_guess) != 1:
            print('Please enter a single letter.')
        elif player_guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif player_guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return player_guess


def displayBoard():
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    if mode == 'TWO-PLAYER':
        blanks = '_' * (len(Game_Word))
        for i in range(len(Game_Word)):  # Replace blanks with correct letters
            if Game_Word[i] in correctLetters:
                blanks = blanks[:i] + Game_Word[i] + blanks[i + 1:]
    else:
        blanks = '_' * (len(Game_Word) - 1)
        for i in range(len(Game_Word) - 1):  # Replace blanks with correct letters
            if Game_Word[i] in correctLetters:
                blanks = blanks[:i] + Game_Word[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


gameIsDone = False
print('H A N G M A N')

# Game Loop
while True:
    displayBoard()

    # Player enters a letter here
    guess = getGuess()
    alreadyGuessed.append(guess)

    # Checks if the guess is correct
    if guess in Game_Word:
        correctLetters.append(guess)

        # Check if player wins
        foundAllLetters = True
        for i in range(len(Game_Word)):
            if Game_Word[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is"' + Game_Word + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters.append(guess)

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard()
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + Game_Word + '"')
            gameIsDone = True
    if gameIsDone:
        break
    else:
        ClearTerminal()
