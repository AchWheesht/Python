import random

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")
print()

#A list of the choices the user can make

commands = ["A. Drink from your canteen.",
    "B. Ahead moderate speed.",
    "C. Ahead full speed.",
    "D. Stop for the night.",
    "E. Status check.",
    "F. Check Commands",
    "Q. Quit."
    ]

game_over = False #A variable that controls the game loop

miles_travelled = 0 #Game progress - game is won at 200 miles
thirst = 0 #Stat - player dies at 6 thirst
drinks = 5 #Resource - player can reset thirst using this resource
camel_tiredness = 0 #Stat - camel dies at 8 tiredness
natives_travelled = -20 #Gane progress - game is lost is this catches up with miles_travelled
game_win = False #After the loop, tells the program if the game was won or lost

for i in range(len(commands)):
    print(commands[i]) #Prints the list of player options

while game_over == False: #Game loop begins here

    print()

    command_input = str.upper(input("Choose your action:\n")) #Player input

    print()

    event_possible = False #Variable to set possibility of random events occuring

    #This long if statement checks inputs, and performs appropriate commands
    if command_input == "Q": #Quit input
        print("You give up, and die in the desert")
        game_over = True
        break
    elif command_input == "E": #Display stats input
        print("Miles travelled:", miles_travelled)
        print("Drinks in canteen:", drinks)
        print("The natives are %s miles behind you" % (miles_travelled - natives_travelled))
        event_possible = False
    elif command_input == "F": #Display commands input
        for i in range(len(commands)):
            print(commands[i])
        event_possible = False
    elif command_input == "D": #Rest for night input
        print("Your camel is happy! The natives gain ground on you")
        camel_tiredness = 0
        natives_travelled += random.randrange(7, 15)
        event_possible = True
    elif command_input == "C": #full speed input
        print("You ride your camel hard! This is thirsty work!")
        miles_travelled += random.randrange(10, 21)
        thirst += random.randrange(1, 4)
        camel_tiredness += random.randrange(1, 4)
        natives_travelled += random.randrange(7, 15)
        event_possible = True
    elif command_input == "B": #Moderate speed input
        print("You ride your camel at a reasonable pace. You travel a fair distsance")
        miles_travelled += random.randrange(5, 13)
        thirst += 1
        camel_tiredness += 1
        natives_travelled += (random.randrange(7, 15))
        event_possible = True
    elif command_input == "A": #drink input
        event_possible = False
        if drinks > 0:
            print("You take a drink from your canteen")
            thirst = 0
            drinks -= 1
        else:
            print("There are no drinks left in your canteen!")
    else: #response to all other inputs
        print("That's not a valid command!")
        event_possible = False

    if thirst >= 4: #Warns player of high thirst - kills player at high thirst
        if thirst <= 6:
            print("You are thirsty!")
        elif thirst > 6:
            print("You died of thirst!")
            game_over = True
        else:
            print("Huh? Your thirst is not determined")

    if camel_tiredness > 5: #Warns player of camel tiredness - kills camel
        if camel_tiredness <= 8:
            print("Your camel is getting tired!")
        elif camel_tiredness > 8:
            print("Your camel drops dead! oh no!")
            game_over = True
        else:
            print("This code is buggy!")

    if natives_travelled >= miles_travelled: #Checks native progress
        print("Oh no! The natives have caught you!")
        game_over = True
    elif (miles_travelled - natives_travelled) < 15:
        print("The natives are getting close!")

    if miles_travelled >= 200: #Checks player progress, can set game win to true
        print(" You have escaped the desert! You go on to lead a happy, carefree life with your stolen camel")
        game_over = True
        game_win = True

    random_event = random.randrange(1, 21)

    if random_event == 1: #Random oasis event
        if event_possible == True:
            print("You find an oasis! You lucky guy!")
            thirst = 0
            canteen = 5
            camel_tiredness = 0

    #game loop ends here

if game_win == False: #Displays how far the player rode if the game was lost
    print("You travelled %s miels before you died" % (miles_travelled))
