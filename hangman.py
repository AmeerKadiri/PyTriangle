import random

def play_hangman():
    words = ["hangman", "computer", "science", "programming", "python"]
    secret_word = random.choice(words)
    guessed_letters = ['_'] * len(secret_word)
    guessed = []
    attempts_left = 6

    while attempts_left > 0:
        print(" ".join(guessed_letters))
        print("Guessed letters:", " ".join(guessed))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha() or guess in guessed:
            print("Invalid guess. Please enter a single letter that hasn't been guessed before.")
            continue

        guessed.append(guess)

        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_letters[i] = guess

            if "_" not in guessed_letters:
                print("Congratulations! You won!")
                break
        else:
            attempts_left -= 1
            print("Incorrect guess. Attempts remaining:", attempts_left)

            if attempts_left == 0:
                print("Game over! The word was:", secret_word)

play_hangman()