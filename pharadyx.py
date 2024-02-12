import fontstyle
import time
import keyboard
import os

def type_text(text, delay=0.0030):
    lines = text.split('\n')
    for line in lines:
        for i, char in enumerate(line):
            # Remove or comment out the spacebar check
            if keyboard.is_pressed('space'):
                print('\r' + line[:i+1], end='', flush=False)  # Clear the current line and re-print characters up to the current position
                keyboard.wait('space', suppress=True)  # Wait for space release
            else:
                print(char, end='', flush=True)
            time.sleep(delay)
        print()  # Print a newline at the end
        os.system("cls")

    
def apply_custom_style(text):
    return f"\033[1;110m{text}\0330m"

title = apply_custom_style("Pharadyx")

class Game:
    @staticmethod
    def check_progress(player_points, total_possible_points):
        progress_percentage = (player_points / total_possible_points) * 100
        if progress_percentage < 30:
            print("You feel not satisfied. Learn more to discover your true self.")
        elif 30 <= progress_percentage < 70:
            print("You sense you are on the right track, but there's still much to uncover.")
        else:
            print("You are making significant progress. Keep going!")

    @staticmethod
    def add_points(player_points, points):
        return player_points + points

    @staticmethod
    def start_game(player_points):
        player_points = 0
        # Add your type_text logic here

def start_game(player_points):
    type_text("Starting a new game...")
    
    # Prologue
    text_list = [
        "He was born with a gift.",
        "A gift that made him different.",
        "Different from everyone else.",
        "He grew up hearing stories about his gift.",
        "Stories that filled him with curiosity and courage.",
        "Stories that told him he had a mission.",
        "He wanted to discover it. He wanted to accomplish it.",
        "He spent his whole life following his gift.",
        "Following the clues and signs that it gave him.",
        "He explored many lands, met many friends, faced many enemies, learned many secrets.",
        "He never gave up. He never stopped trying.",
        "But he never reached it.",
        "He never reached the end of his journey. The end of his mission.",
        "He always found himself back at the beginning. Back where he started.",
        "He grew old and wise. He realized he had lived many lives.",
        "He realized he had learned many lessons.",
        "He realized he had a choice.",
        "He died with a gift.",
        "A gift that could change everything, but nothing.",
        "But he was not a failure.",
        "He was not a waste. He was a hero.",
        "A hero who inspired many. A hero who touched many.",
        "A hero who gave many a gift.",
        "A gift that could change everything, and something."
    ]

    # Display the prologue using type_text for each line
    for line in text_list:
        type_text(line)

            
    # Clear the screen
    os.system("cls")

    # Start Chapter I)
    chapter_i()

   
def quit_game():
    print(type_text("Quitting the game..."))
    
def menu():
    user_input = ""
    # A while loop to repeat the menu
    while user_input not in ["1", "Q"]:
        print(title)
        print("1. Start a new game")
        print("Q. Quit the game")
        user_input = input("> ")
        if user_input == "1":
            # Start a new game
            start_game(player_points = 0)
        elif user_input.lower() == "q":
            # Quit the game
            quit_game()
        else:
            print("Invalid input. Please try again.")
            user_input = ""

def chapter_i():
    
    # Chapter I text
    chapter_i_text = [
    "You wake up in a room. It looks familiar, but not quite.",
    "It's your childhood room, but something is off.",
    "You see a story book. It's old and faded. You recognize it.",
    "You pick it up and open it. The pages are blank. You wonder why.",
    "Your mom knocks on the door and comes in. She sees the book in your hands.",
    "She says dinner is ready and you need to come downstairs. Now.",
    "You show her the book and ask her if she remembers it.",
    "She says she used to read it to you when you were little. One of your favorites.",
    "She says she doesn't know what happened to the pages. They must have worn off over time.",
    "She says it doesn't matter. You need to let go of the past.",
    "You follow her downstairs. You smell something burning.",
    "As you reach the bottom of the stairs, you see a fire outside the window.",
    "You see a blast of flames and smoke. Your mom pushes you to the kitchen.",
    "You are horrified. You look through the window and see a swarm of men in black suits.",
    ]
    for line in chapter_i_text:
        type_text(line)
    
    while True:
        print("Press E to continue")
        user_input = input("> ").lower()

        if user_input == "e":
            break
        else:
            print("Invalid input. Please press 'E' to continue.")

    os.system("cls")
    
       
    # Choices loop
    while True:
        print("\nWhat should you do next?")
        print("1. Stay hidden")
        print("2. Sneak away with your mom")

        choice = input("> ")

        if choice == "1":
            choice_a1()
            break
        elif choice == "2":
            choice_a2()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
        os.system("cls")

def choice_a1():
    choice_a1_text = [
    "You choose to silently sneak into the nearby pantry, leaving the door slightly open to watch the situation.",
    "From your hiding place, you can catch the soldiers' conversation and see flashes of their actions.",
    "The leader, whom you don't know, appears to be in command, talking about their mission mysteriously.",
    "He seems familiar, but you don't know where.",
    "They say something about finding the boy is their only goal.",
    "Your mom, trying to save you, says that you're not here.",
    "The soldiers, doubtful, started asking her about your location.",
    "You keep quiet, hoping she can keep up the lie.",
    "The pressure in the pantry rises as the men push her for information.",
    "Despite her attempts, the soldiers begin to search the house more carefully.",
    "Two men comes near the pantry.",
    "They sound annoyed and tired. They talk about their mission and why they are here.",
    "You want to hear more, but the information is scarce.",
    "You want to escape, but you must find a way",

    ]

    for line in choice_a1_text:
        type_text(line)
    
    while True:
        print("Press E to continue")
        user_input = input("> ").lower()

        if user_input == "e":
            break
        else:
            print("Invalid input. Please press 'E' to continue.")
    os.system("cls")
    
    # Choices loop
    while True:
        print("\nWhat should you do next?")
        print("1. Listen silently")
        print("2. Create distraction")

        choice = input("> ")

        if choice == "1":
            choice_a1a()
            break
        elif choice == "2":
            choice_a1b()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    

def choice_a1a(player_points):
    choice_a1a_text = [
        "''...I can't take it anymore, man. We're stuck in this, doing the same thing over and over.''",
        "''Yeah, and he's just gone crazy, talking about some grand plan that never seems to work.''",
        "''I mean, how long are we supposed to keep this up?''",
        "''He's crazy, man. Lost it ages ago. But you know how he gets when someone questions him.''",
        "''I just want out. There's no end to this madness.''",
        "You hear them and feel shocked.",
        "You move a bit and make a noise.",
        "The men stop talking, looking at where you are.",
        "You feel scared and trapped. You don't know what to do.",
    ]

    for line in choice_a1a_text:
        type_text(line)

    updated_points = Game.add_points(player_points, 20)

    while True:
        print("Press E to continue")
        user_input = input("> ").lower()

        if user_input == "e":
            break
        else:
            print("Invalid input. Please press 'E' to continue.")
        os.system("cls")

    # Choices loop
    while True:
        print("\nWhat should you do next?")
        print("1. Climb through the window")
        print("2. Hide in the shed")

        choice = input("> ")

        if choice == "1":
            game_continues = choice_a1a1(updated_points)
            if not game_continues:
                return False
            break
        elif choice == "2":
            game_continues = choice_a1a2(updated_points)
            if not game_continues:
                return False
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
        os.system("cls")

    return True

def choice_a1a1(player_points):
    choice_a1a1_text = [
        "You choose the window, opening the window and jumping out.",
        "You land on the soft grass in the backyard.",
        "You sprint to the other side of the house, looking for a way out.",
        "The men, delayed by the window, lose sight of you.",
        "You manage to escape, leaving them in the dark.",
        "You wonder about their mission and why they feel like entrapped.",
        "You wonder if you are part of it too.",
    ]
    for line in choice_a1a1_text:
        type_text(line)

    return True

def choice_a1a2(player_points):
    choice_a1a2_text = [
        "You spot a shed and dash inside, praying they won't find you.",
        "But the shed door squeaks loudly.",
        "They notice it and head to the shed.",
        "They open the door and see you cowering inside.",
        "You are cornered and surrounded. You have no chance of escape.",
        "You have made a fatal mistake.",
        "Game over.",
    ]

    for line in choice_a1a2_text:
        type_text(line)

    while True:
        print("\nWhat should you do next?")
        print("1. Climb through the window")
        print("2. Hide in the shed")

        choice = input("> ")

        if choice == "1":
            game_continues = choice_a1a1(player_points)
            if not game_continues:
                return False
            break
        elif choice == "2":
            game_continues = choice_a1a2(player_points)
            if not game_continues:
                return False
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    return True
   
def choice_a1b():
        choice_a1b_text = [
        "You decide to create a distraction, so you grab a can from the pantry and toss it across the hallway.",
        "It hits the wall and makes a loud noise.",
        "The two men pause their conversation and turn their heads.",
        "They wonder what the noise was and where it came from.",
        "You use this moment to slip out of the pantry and sneak past them.",
        ]

        for line in choice_a1b_text:
            type_text(line)
    
        while True:
            print("Press E to continue")
            user_input = input("> ").lower()
            
            if user_input == "e":
                break
            else:
                print("Invalid input. Please press 'E' to continue.")
            os.system("cls")

        # Choices loop
        while True:
            print("\nWhat should you do next?")
            print("1. Go to the basement")
            print("2. Go upstairs")

            choice = input("> ")

            if choice == "1":
                choice_a1b1()
                break
            elif choice == "2":
                choice_a1b2()
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
            os.system("cls")

def choice_a1b1():
                choice_a1b1_text = [
                "You choose to go to the basement. You go down into the dark and cold basement.",
                "The air is thick, and you only hear your steps on the floor.",
                "You look around the dark space, and see a door in a corner.",
                "You go to the door, and open it slowly. Behind it is a small hall with a light at the end.",
                "You hear water dripping in the hall. You walk through the hall, and find another door. It is open a bit.",
                "You open this door and go to the backyard.",
                "You get out of the basement, you escaped.",
                "For now..."
                ]

                for line in choice_a1b1_text:
                    type_text(line)

def choice_a1b2(player_points):
        choice_a1b2_text = [
            "You choose to go upstairs. You go up quietly, carefully.",
            "You get to the upper floor and look for a window to get out.",
            "There are two men in your room, so you get into another room.",
            "They did not see you. In the room, you find the same storybook on a shelf.",
            "It must be a copy. You grab the book and go to the window, hoping to get away.",
            "The window is slightly open, and the air is chilly.",
            "You push the window more, see a tree nearby and jump on it, climbing down.",
            "You escape from the house."
        ]

        for line in choice_a1b2_text:
            type_text(line)

        # Update points
        updated_points = Game.add_points(player_points, 20)


 

def choice_a2():
    choice_a2_text = [
    "You tell your mom to hide with you.",
    "She wants you to follow her before they break into the house.",
    "You follow your mom, and you both go quietly through the house, finding a secret way to the basement.",
    "You wonder how there is a secret way, and how your mom knows it.",
    "Your mom knows where to go, and takes you to a door in a corner.",
    "You open the door carefully, and see a small hall.",
    "You hear water dripping as you walk through the hall, and find another door at the end.",
    "You open it, and go to the backyard.",
    "You and your mom go to the car nearby. The car starts well, and you leave the house.",
    "They heard you and start to chase you.",
    "While running away from them, you have lots of questions you want to ask your mom...",
    ]
    for line in choice_a2_text:
            type_text(line)
    
    while True:
            print("Press E to continue")
            user_input = input("> ").lower()

            if user_input == "e":
                break
            else:
                print("Invalid input. Please press 'E' to continue.")
            os.system("cls")

        # Choices loop
    while True:
        print("1. Who are those men and why are they after us?")
        print("2. How do you know about the secret way to the basement?")

        choice = input("> ")

        if choice == "1":
            choice_a2a(player_points = 0)
            break
        elif choice == "2":
            choice_a2b()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
        os.system("cls")

def choice_a2a(player_points):
    choice_a2a_text = [
        "''...I don't know. I heard them talking about this book.",
        "''Something that they think is in the book you found.''",
        "''At first I thought they are usurers. But what would they do with the book?"
        "It is just one of the books from your childhood.",
        "She speaks with tension and fear in her voice.",
        "You feel she is hiding something."
    ]

    for line in choice_a2a_text:
        type_text(line)

    # Update points
    updated_points = Game.add_points(player_points, 20)

    
def choice_a2b():
        choice_a2b_text = [
        "''I discovered the secret passages when we first moved in here.''",
        "You wouldn't remember because your were a child.",
        "''It might be related to something old owner needed.",
        "''I never expected we would need them for something like this.''",
        "Her face does not look surprised."
        ]
        
        # Choices loop
        while True:
            print("1. If it is about the book, why are they after me then?")
            print("2. What is this book really about?")
            choice = input("> ")

            if choice == "1":
                choice_a2a1()
                break
            elif choice == "2":
                choice_a2a2()
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
            os.system("cls")

def choice_a2a1():
            choice_a2a1_text = [
            "''...I don't know. I heard the same things as you.",
            "Her eyes reflecting a mix of fear and regret.",
            "Trust me, we need to...",
            "The sentence hangs in the air, shattered by the sudden crash."
            "The voices around you blur, and you're on the verge of passing out.",
            "The crash leaves an overwhelming smell of burning rubber in the air.",
            "Your vision blurs, and your whole body aches with a dull, persistent pain.",
            "Everything feels hazy, but you hear your mom."
            "'' We will meet again, wait for me!''"
            "You passed out..."
            ]

            for line in choice_a2a1_text:
                type_text(line)


def choice_a2a2():
            choice_a2a2_text = [
                "''Maybe the book is more than it seems.''",
                "The sentence hangs in the air, shattered by the sudden crash."
                "The voices around you blur, and you're on the verge of passing out.",
                "The crash leaves an overwhelming smell of burning rubber in the air.",
                "Your vision blurs, and your whole body aches with a dull, persistent pain.",
                "Everything feels hazy, but you hear your mom."
                "'' We will meet again, wait for me!''"
                "You passed out..."
            ]



# Call the menu function to start the program
menu()

