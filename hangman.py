import random
from words import wordList

def getWord():
    word = random.choice(wordList)
    return word.upper()

def startGame(word):
    guessedLetters = []
    guessedWords = []
    numGuesses = 6
    wordToShow = "_" * len(word)
    foundWord = False

    print(display(numGuesses))
    print(wordToShow)
    print("\n")

    while not foundWord and numGuesses > 0:
        guess = input("Please enter a letter or a word as a guess: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                numGuesses -= 1
                print("Sorry, you've already tried that! ")
            elif guess not in word:
                numGuesses -= 1
                print("Sorry, that's not correct. Try again! ")
                guessedLetters.append(guess)
            else:
                print("Nice work!")
                guessedLetters.append(guess)
                wordAsList = list(wordToShow)
                indicies = [i for i, letter in enumerate(word) if letter == guess]
                for index in indicies:
                    wordAsList[index] = guess
                wordToShow = "".join(wordAsList)
                if "_" not in wordToShow:
                    foundWord = True
                    print("YOU WIN!!")
        elif len(guess) == len(word):
            if guess in guessedWords:
                numGuesses -= 1
                print("Sorry you've already tried that!")
            elif guess != word:
                numGuesses -= 1
                print("Sorry, that's not correct, Try again! ")
                guessedWords.append(guess)
            else:
                foundWord = True
                print("That's correct! You Win!")
                wordToShow = word
        else:
            print("Sorry, invalid input. Try again! ")
            numGuesses -= 1
        print(display(numGuesses))
        print(wordToShow)
        print("Guessed Letters: ")
        print(*guessedLetters, sep=" ")

    if numGuesses == 0:
        print("You Lose!")
        print("The word was", word)
    else:
        print("Way to go! You won!")

def display(numGuesses):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[numGuesses]

def main():
    word = getWord()
    startGame(word)
    while input("Do you want to play again? Y/N ") == "y":
        word = getWord()
        startGame(word)

if __name__ == "__main__":
    main()