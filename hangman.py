import random


def choose_word():
    words = [
        "snake",
        "hey",
        "list",
        "bunny",
        "log",
        "apple",
        "me",
        "you",
        "great",
        "my",
        "hello",
        "amazing",
        "i",
        "log",
        "list",
        "pneumonoultramicroscopicsilicovolcanoconiosis",
        "aeon"
    ]
    return random.choice(words)


def display_hangman(attempts):
    hangman_pics = [
        """
          +---+
          O   |
         /|\  |
         / \  |
             ===
        """,
        """
          +---+
          O   |
         /|\  |
         /    |
             ===
        """,
        """
          +---+
          O   |
         /|\  |
              |
             ===
        """,
        """
          +---+
          O   |
         /|   |
              |
             ===
        """,
        """
          +---+
          O   |
          |   |
              |
             ===
        """,
        """
          +---+
          O   |
              |
              |
             ===
        """,
        """
          +---+
              |
              |
              |
             ===
        """
    ]

    return hangman_pics[attempts]


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")

    while True:
        print(display_hangman(attempts_left))
        print(display_word(word_to_guess, guessed_letters))

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word: ", word_to_guess)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if guess not in word_to_guess:
                attempts_left -= 1
                print("Incorrect guess. Attempts left:", attempts_left)
                if attempts_left == 0:
                    print("Sorry, you ran out of attempts. The word was:", word_to_guess)
                    break


if __name__ == "__main__":
    hangman()
