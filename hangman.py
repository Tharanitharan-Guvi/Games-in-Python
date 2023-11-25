import random

def choose_word():
    words = ["python", "guvi", "programming"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

word_to_guess = choose_word()
guessed_letter = []
attempt = 5

while attempt > 0:
    current = display_word(word_to_guess, guessed_letter)
    print("Current Word: ", current)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letter:
        attempt -= 1
        print("You have already guessed that letter. Try again!")
    
    else:
        guessed_letter.append(guess)

        
        if "_" not in display_word(word_to_guess, guessed_letter):
            print("Congratualtions! You have guessed the word correctly.")
            print("The correct word is", word_to_guess)
            break
        elif guess in word_to_guess:
            print("Congratualions! The", guess, "is present in the word")
        else:
            attempt -= 1
            print("Incorrect! You have", attempt, "attempts remaining")

if attempt == 0:
    print("Sorry, you are out of attempts, the word was: ", word_to_guess)