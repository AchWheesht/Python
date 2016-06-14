Hi Johnny! Here's an inventory;

all file beginning with game_ are part of the game.
 
game_game is the main file, have a look in there first.

game_nobles is the biggest and most complicated file by far.

IDLE controller just contains the line "import game_game". It lets me run game_game easily while
editing it in ATOM (instead of editing it in IDLE)

event_database writer isn't important right now.

noblename_app is a standalone version of the function "generate_noble_name" in game_nobles. Try it out!

noblenames_database_writer is a file that i use to store the various names and such that noblename_app and 

generate_noble_name use. This is so I don't have to write a txt file in JSON.

test is a file i use for testing concepts in python. its my "does this idea actually work?" file

noblenames.txt is what noblesnames_database_writer writes to

nobles_dict stores all the nobles the game has generated (noblename_app does not use this)

