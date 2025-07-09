import random
word_list = ["apple", "tiger", "chair", "robot", "plant"]
word_to_guess = random.choice(word_list)
guessed_letters = []
tries_left = 6
def display_word():
    display = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
print("🎮 Welcome to Hangman!")
while tries_left > 0:
    print("\nWord to guess: ", display_word())
    print(f"Tries left: {tries_left}")
    guess = input("Enter a letter: ").lower().strip()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Correct guess!")
    else:
        print("❌ Wrong guess!")
        tries_left -= 1

    if all(letter in guessed_letters for letter in word_to_guess):
        print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
        break
else:
    print("\n💀 Game Over! The word was:", word_to_guess)