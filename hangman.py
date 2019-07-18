import random

# A list of words that
potential_words = ["music", "nap", "girl", "code"]

word = random.choice(potential_words)
lengthofword = (len(word))# Use to test your code:

#print(word)

# Converts the word to lowercase

# Make it a list of letters for someone to guess

current_word = [] # TIP: the number of letters should match the word
# Some useful variables
word = word.lower()
for letter in word:
    current_word.append("_")

#correctanswer = ["m", "u", "s", "i", "c", "n", "a", "p", "g", "r", "l", "o", "d", "e"]

guesses = []
maxfails = len(word) + 2
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ")
    #while guess not in guesses:
        #guesses.append(guess)
    if guess == word:
        print ("you win!")
        break
    elif guess in word:
        print("guesses correctly!")
        for let in range(len(word)):
            if word[let] == guess:
                print(word[let])
                current_word[let] = guess
    else:
        print("guessed wrong!")
        fails = fails+1
        print("You have " + str(maxfails - fails) + " tries left!")

    print(current_word)

    if not "_" in current_word:
        print("You win")
        break

    	# check if the guess is valid: Is it one letter? Have they already guessed it?

    	# check if the guess is correct: Is it in the word? If so, reveal the letters!
