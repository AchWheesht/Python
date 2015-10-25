room_list = [
    ["This is Phil's Bedroom", None, None, 2, None],
    ["This is Paul's Room", None, 2, 3, None],
    ["This is the Hallway", 0, 5, 4, 1],
    ["This is the Kitchen", 1, None, None, None],
    ["This is Gavin's Room", 2, 6, None, None],
    ["This is the shared bathroom", None, None, None, 2],
    ["This is the en-suite bathroom", None, None, None, 4]
    ]


directions = [
    None,
    "There is a Passage to the North",
    "There is a Passage to the East",
    "There is a Passage to the South",
    "There is a Passage to the West"
    ]

commands = [
    None,
    "north",
    "east",
    "south",
    "west"
    ]

game_running = True
current_room = 0


while game_running:
    current_room_stats = room_list[current_room]

    print()
    print("***%s***" % (current_room_stats[0]))
    print()
    for i in range(len(current_room_stats)):
        if current_room_stats[i] != None:
            if directions[i]:
                print(directions[i])
    print()

    confirmed_action = None
    room_movement = None
    while not confirmed_action:
        action_move = str.lower(input("Which direction would you like to move?\n"))
        if action_move == "quit":
            game_running = False
            break
        for i in range(len(commands)):
            if action_move == commands[i]:
                if current_room_stats[i] != None:
                    confirmed_action = action_move
                    room_movement = current_room_stats[i]
        if not confirmed_action:
            print("That is not a valid command")
    if confirmed_action:
        print("You are moving %s" % (confirmed_action))
    current_room = room_movement
