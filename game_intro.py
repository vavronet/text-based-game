import time

def run():
    print("Welcome to The Heart-Hands and the Pants!\n")

    avatar = input("Enter your avatar name here: \n")

    print("\nGrettings, {}!\nThe kingdom of pants has been conquered by the evil hat masterminds!\nSave the pant people and defeat the evil hat wizard! \nMay the odds be with you Heart-Hand!".format(avatar))

    time.sleep(3)

    print("How to Play:\nEach boss you encounter will have a certain amount of health points or HP, which determines how hard the boss is.\n")
   
    time.sleep(1)
   
    print("In order to defeat your opponets you have to attck them.\nYou have 10 tries to defeat your enemny and each hit is a random number between 0 and 10.\nThere is a higher probibility that you will get higher numbers than lower ones.")

    time.sleep (1)

    print("\nEverytime you finish a turn, the boss will also attack you using the same fighting system except as the bosses increase, their attcks also become greater.\n")

    input('Are you ready to begin your mission? (Press Enter)\n')

    