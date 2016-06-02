import random
import time
import json
import os

class resources:
    def __init__(self):
        self.supplies = {}
        self.events = {}
        self.is_alive = True
        self.filename = "events_dict.json"
        if os.path.isfile(self.filename):
            self.load_file()

    def load_file(self):
        with open(self.filename, "r") as file:
            coded = file.read()
        self.events = json.loads(coded)
            
    def save_file(self):
        coded = json.dumps(self.events)
        with open(self.filename, "w") as file:
            file.write(coded)
            
class events:
    def __init__(self):
        self.event_list = {
            1: "famine",
            2: "drought",
            3: "asphyxiation",
            4: "year_of_plenty",
            5: "uneventful_year"
            }
        self.events = {}
        self.filename = "events_dict.json"
        if os.path.isfile(self.filename):
            self.load_file()

    def load_file(self):
        with open(self.filename, "r") as file:
            coded = file.read()
        self.events = json.loads(coded)
            
    def save_file(self):
        coded = json.dumps(self.events)
        with open(self.filename, "w") as file:
            file.write(coded)

    def new_basic_event(self):
        new_event = {}
        new_event_name = input("What is the event called?")
        new_event["name"] = new_event_name
        while True:
            new_event_description_temp = input("Enter the event's description")
            validate_description = input("Is this description correct? (y/n)\n" + new_event_description_temp)
            validate_description = str(validate_description).lower()
            if validate_description == "y":
                new_event_description = new_event_description_temp
                break
        new_event["description"] = new_event_description
        event_choices_count = int(input("How many choices does the event have?"))
        event_choices = {}
        for i in range(event_choices_count):
            choice_text = input("What is the text for choice " + str(i + 1) + "?")
            event_choices["choice " + str(i + 1)] = choice_text
            stats_count = int(input("How many stats does this choice affect?"))
            stats_affected = {}
            for n in range(stats_count):
                while True:
                    stat = input("Which stat is stat " + str(n + 1) + "?")
                    sign = input("How is it affected? (+. -. *. /)")
                    value = input("By how much is it affected?")
                    final_string = stat + " " + (sign) + " " + str(value)
                    is_ok = input(final_string + ". Is this ok? y/n")
                    if is_ok == "y":
                        break
                stats_affected["effect " + str(n + 1)] = final_string
            event_choices["outcome " + str(i + 1)] = stats_affected
        final_dict = {**new_event, **event_choices}
        print("Check Results")
        print("Name: " + final_dict["name"])
        print("Description: " + final_dict["description"])
        for i in range(event_choices_count):
            stats_dict = final_dict["outcome " + str(i + 1)]
            print("Choice " + str(i + 1) + " text: " + final_dict["choice " + str(i + 1)]),
            for k, v in stats_dict.items():
                  print(k + ", " + v)
        print("")
        is_ok = input("Is this ok? y/n")
        if is_ok == "y":
            self.events[new_event_name] = final_dict
            self.save_file()
        
    def run_random_event(self):
        event_id = random.randint(1, 5)
        event_id = 1
        holder = getattr(self, self.event_list[event_id])
        holder()

    def status_check(self):
        if player.supplies["Food"] <=0:
            player.is_alive = False
        elif player.supplies["Water"] <= 0:
            player.is_alive = False
        elif player.supplies["Air"] <= 0:
            player.is_alive = False
            
    def famine(self):
        print("Famine! Your crop yields are low this year. Choose one:")
        print(" a) Lose half your food, gain one water and one air")
        print(" b) lose 3 food")
        print(" c)Lose two food, one water and one air")
        resolved = False
        while resolved == False:
            choice = input("What is yor choice?")[0]
            choice = choice.lower()
            if choice == "a":
                player.supplies["Food"] = int(player.supplies["Food"] / 2)
                player.supplies["Water"] = player.supplies["Water"] + 1
                player.supplies["Air"] = player.supplies["Air"] + 1
                resolved = True
            elif choice == "b":
                player.supplies["Food"] = player.supplies["Food"] - 3
                resolved = True
            elif choice == "c":
                player.supplies["Food"] = player.supplies["Food"] - 1
                player.supplies["Water"] = player.supplies["Water"] - 1
                player.supplies["Air"] = player.supplies["Air"] -1
                resolved = True
            else:
                print("Wow, really? It's one of, like, three letters. Try harder, idiot")
        print("Your resources are now:")
        print("Food: " + str(player.supplies["Food"]))
        print("Water: " + str(player.supplies["Water"]))
        print("Air: " + str(player.supplies["Air"]))
        self.status_check()

player = resources()

player.supplies["Food"] = 10
player.supplies["Water"] = 10
player.supplies["Air"] = 10
        
events = events()

while player.is_alive == True:
    command = input("What now? (Run event, New event, Display stats, Quit)")
    command = command.lower()
    if command == "quit":
        break
    elif command == "display stats":
        print("Your resources are:")
        print("Food: " + str(player.supplies["Food"]))
        print("Water: " + str(player.supplies["Water"]))
        print("Air: " + str(player.supplies["Air"]))
    elif command == "run event":
        events.run_random_event()
    elif command == "new event":
        events.new_basic_event()
    else:
        print("Not a valid command, dude")

if player.is_alive == False:
    print("Game over, man, game over!")

while player.is_alive == False:
      time.sleep(3)
      print("YOU LOSE")

