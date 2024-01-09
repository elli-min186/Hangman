import random


def word_to_play(filename):
    with open(filename, 'r') as file:  # open this filename as file with read only
        words = file.readlines()  # read each line from the file
        return random.choice(words).strip()  # choose random word from the words list


def playgame(word, guessed):  # give _ by the count of word to guess and show the word if correctly guessed
    wordtoguess = ""
    for letter in word:
        if letter in guessed:
            wordtoguess += letter + " "
        else:
            wordtoguess += "_ "
    return wordtoguess


def hangman():
    word = word_to_play("words.txt")
    guessed = []
    attempts = 6
    print("Welcome to the game of life or death. \nYou have been kidnapped by your enemy who loves to copy your code and "
          "they are planning to get rid of you."
          "\nThis is your only way of surviving:"
          "\nI will be choosing a random word from my word list and it is your job to guess the right one."
          "\nIf you don't, well, goodbye...")
    prompt = input("Are you ready for your only chance of surviving? (yes/no): ").lower()

    wordtoguess = playgame(word, guessed)

    if prompt == "no":
        print("I guess you still have no gut for this kind of adventure. Say hi to my friend if you see him in hell.")
    elif prompt == "yes":
        print(wordtoguess)

        while attempts > 0:
            inputword = input("Guess one letter in the word: ").lower()

            if len(inputword) != 1 or not inputword.isalpha():
                print("I said a letter L E T T E R")
                continue

            if inputword in guessed:
                print("You've already guessed that letter")
                continue

            guessed.append(inputword)

            if inputword not in word:
                attempts -= 1
                print("Wrong Guess, Try Again")

                if attempts == 1:
                    print("Last chance to survive")

                else:
                    print("You have {} attempts left.".format(attempts))

                if attempts == 0:
                    print("Well, too late! The word is: ", word)
                    break
            else:
                print("No way, you are guessing that fast")

            wordtoguess = playgame(word, guessed) #update _ with correct guess
            print(wordtoguess)

            if "_ " not in wordtoguess:
                print("Dang it... You managed to free yourself... Yay")
                break

        playagain = input("Do you want to play again? (yes/no): ").lower()
        if playagain == "no":
            print("Thank you for playing. Have a nice day")

        elif playagain == "yes":
            hangman()


if __name__ == "__main__":
    hangman()
