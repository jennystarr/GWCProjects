# --- Define your functions below! ---
def intro():
    print("Hello this is a thing I am working on, please do not make fun of me.")
    print("I am very new to the coding life.")
def process_input(answer):
    if answer == "hi":
        say_greeting()
    else:
        say_default()

def say_greeting():
    print("hey welcome!")

def say_default():
    print("very cool!")


def sayingpart():
    print("python for me was kinda hard to understand.")
    print("how about you?")
def conversation(answer2):
    if answer2 == "easy":
        say_lineone()
    else:
        say_linetwo()

def say_lineone():
    print("Well... that is good for you. You are a smarty pants... I however, am not.")

def say_linetwo():
    print("Well that is okay, it will become easy overtime.")


def anotherline():
    print("so, do you want to play a game? If you do type 'yes'")
def talking(answer3):
    if answer3 == "yes":
        say_fine()
    else:
        say_notfine()

def say_fine():
    print("okay so do you want an adventure game or hangman?")
    print("Type 'adventure game' to go to the adventure game type 'hangman' to play hangman.")
    user_input = input()
    if user_input == "adventure game":

        # Update this text to match your story.
        start = '''
        One day Christopher Robina and Pooh were bored.
        They had to make a decision to go to the park or a tea party.
        '''
        print(start)

        print("Type 'park' to go to the park or 'tea party' to go a tea party.") # Update to match your story.
        user_input = input()
        if user_input == "park":
            print("You decide to go the park and meet Piglet there. Pooh asks if he wants to join their soccer match. Piglet agrees and they have an intense match. Pooh breaks Christopher Robin's ankles. After they finish Christopher Robin asks pooh if he wanted to nap or go to a tea party.") # Update to match your story.
            print("Type 'nap' to go to the bedroom or 'tea party' to go to a tea party.")
            user_input = input()
            if user_input == "nap":
                print("The trio goes back home and decide to have a sleepover in Pooh's room")
            elif user_input == "tea party":
                print("You choose to go to the tea party and meet Rabbit, who joins them.  Rabbit spills the tea about his neighbors.Pooh hypes him up to go say smething to their faces. After they are all satisfied, Christopher Robin asks Pooh if he wants to go to the nap or jungle.") # Update to match your story.
                user_input = input()
                if user_input == "nap":
                    print("The trio goes back home and decide to have a sleepover in Pooh's room. They watched movies until midnight.")
                elif user_input == "jungle":
                    print("Christopher Robin and Pooh goes to the jungle and play tag with Tigger. Tigger gets lost because it was too dark t look for him. Christoper Robin and Pooh give up finding him for the day for the rest of the day and will search for him tomorrow.")

            # Continue code to finish story.

        elif user_input == "tea party":
            print("You choose to go to the tea party and meet Rabbit, who joins them. After they are all satisfied, Christopher Robin asks Pooh if he wants to go to the park or jungle.") # Update to match your story.
            print("type 'nap' to go back home and sleep or 'jungle' to go to the jungle.")
            user_input = input()
            if user_input == "nap":
                print("The trio goes back home and decide to have a pillow fight. Piglet ended up with a bloody nose so they all stopped and had a sleepover in Pooh's room. Intead of sleeping they were playing cards till morning.")
            elif user_input == "jungle":
                print("Christopher Robin and Pooh goes to the jungle and play tag with Tigger. Tigger gets lost because it was too dark t look for him. Christoper Robin and Pooh give up finding him for the day for the rest of the day and will search for him tomorrow.")

            # Continue code to finish story.
    if user_input == "hangman":
        import random

        # A list of words that
        potential_words = ["music", "nap", "girl", "code"]

        word = random.choice(potential_words)
        lengthofword = (len(word))# Use to test your code:

        current_word = [] # TIP: the number of letters should match the word

        word = word.lower()
        for letter in word:
            current_word.append("_")

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


def say_notfine():
    print("okay, next time if you want to just type yes.")


def sports():
    print("I play a lot of sports.")
def soccertalk(answer4):
    if answer4 == "yes":
        same_girl()
    else:
        sorryforyou()

def same_girl():
    print("Yo I love sports! It is so fun with friends and if you win it feels nice :) ")

def sorryforyou():
    print("Maybe you should give it a try. You will never know if you do not try right?")

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?)")
        process_input(answer)
        print("so let me tell you something!")
        break
    sayingpart()
    while True:
        answer2 = input("(Your response?)")
        conversation(answer2)
        print("I promise!")
        break
    anotherline()
    while True:
        answer3 = input("(What is your answer?)")
        talking(answer3)
        print("thank you for staying this long!!!")
        break
    sports()
    while True:
        answer4 = input("(what about you?)")
        soccertalk(answer4)
        print("great")
        break



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
