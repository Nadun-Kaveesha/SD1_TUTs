secret_word = "apple"
turns = 1
guessed_letters = []

print("Let's play Guessing game")
print(f'You have {len(secret_word) + 3} turns to guess the word!')
print("_ " * len(secret_word))

while True:
    if turns <= len(secret_word) + 3:
        guess = str(input("\nMake your guess: "))

        for letter in secret_word:
            if letter in guessed_letters or letter == guess:
                print(f' {letter} ', end='')
                if letter not in guessed_letters:
                    guessed_letters.append(letter)
            else:
                print('_ ', end='')

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            break

        turns += 1
    else:
        print("\nSorry, your turns are over!")
        break
