import random

def choose_word():
    words_with_hints = [
        ("elephant", "The largest land animal with a long trunk and big ears."),
        ("symphony", "A grand musical performance with an orchestra."),
        ("bicycle", "A two-wheeled vehicle powered by pedals."),
        ("paradox", "A statement that contradicts itself but may still be true."),
        ("galaxy", "A vast system of stars, gas, and dust held together by gravity."),
        ("quixotic", "Describing someone who pursues unrealistic and impractical ideals."),
        ("zephyr", "A gentle breeze or light wind."),
        ("hyacinth", "A fragrant flower that blooms in clusters on a tall stem."),
        ("acoustic", "Relating to sound or the sense of hearing, often used with musical instruments."),
        ("labyrinth", "A complex maze with intricate passages and blind alleys."),
        ("pinnacle", "The highest point or peak of achievement."),
        ("xylophone", "A musical instrument with wooden bars that produce different tones when struck."),
        ("chimera",
         "In mythology, a creature with parts from different animals; also used to describe an unrealistic dream or hope."),
        ("nebula", "A cloud of gas and dust in space, often where stars are born."),
        ("quasar", "A celestial object that emits massive amounts of energy and light."),
        ("ephemeral", "Something short-lived or lasting for only a brief period."),
        ("velociraptor", "A small, predatory dinosaur with a name that means 'swift thief'."),
        ("iridescent", "Displaying colors that change depending on the angle of view."),
        ("epiphany", "A sudden and profound realization or understanding."),
        ("quotidian", "Referring to everyday activities or ordinary occurrences."),
    ]

    return random.choice(words_with_hints)

def display_hangman(attempts):
    hangman_pics = [
        """
          +---+
              |
              |
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
          O   |
          |   |
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
         /|\  |
              |
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
         / \  |
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
    word_to_guess, hint = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Hint:", hint)

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

