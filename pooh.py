
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
