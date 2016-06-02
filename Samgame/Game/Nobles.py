import json
import os
import random
import time

class DictNobles:

    def __init__(self):
        self.nobles = {}
        self.filename = "nobles_dict.json"
        if os.path.isfile(self.filename):
           self.load_file() 
        
    def view_all(self):
        print("")
        for k, v in self.nobles.items():
            print("Name: " + k + ". Stats: " + str(v))
        print("")
 
    def get_stats(self):
        while True:
            request = input("Request whose stats/cancel?)")
            if request == "cancel":                              
                print("Operation Cancelled")
                return
            try:
                hold = self.nobles[request]
                print(str(hold))
                return
            except KeyError:
                print("Name not in database")

    def create_noble(self):
        name = input("What is the Nobles name?")
        intel = int(input("What is the Nobles intelligence? (0 - 10)"))
        ambition = int(input("What is the Nobles ambition? (0 - 10)"))
        network = int(input("How strong is the Nobles network? (0 - 10"))
        wealth = int(input("How wealthy is the Noble? (0 - 10)"))
        
        stats = {
            "intel": intel,
            "ambition": ambition,
            "network": network,
            "wealth": wealth,
        }
        self.nobles[name] = stats
        
        self.save_file()
        print("")
        print("New noble added! Name: " + str(name) + ", Intelligence: " + str(intel) + ", Ambition: " + str(ambition) + ", Network:" + str(network) + ", Wealth: " + str(wealth))
        print("")

    def create_random_noble(self):
        name = input("What is the Nobles name?")
        intel = int(round(random.triangular(0, 10)))
        ambition = int(round(random.triangular(0, 10)))
        network = int(round(random.triangular(0, 10)))
        wealth = int(round(random.triangular(0, 10)))
        
        stats = {
            "intel": intel,
            "ambition": ambition,
            "network": network,
            "wealth": wealth,
        }
        self.nobles[name] = stats
        
        self.save_file()
        print("")
        print("New noble added! Name: " + str(name) + ", Intelligence: " + str(intel) + ", Ambition: " + str(ambition) + ", Network:" + str(network) + ", Wealth: " + str(wealth))
        print("")
        
    def remove_noble(self):
        while True:
            hold = input("Delete which noble/cancel?")
            if hold == "cancel":
                print("Operation Cancelled")
                return
            try:
                del self.nobles[hold]
                self.save_file()
                print("")
                print(hold + " deleted.")
                print("")
                return
            except KeyError:
                print("Name not in database")

    def save_file(self):
        coded = json.dumps(self.nobles)
        with open(self.filename, "w") as file:
            file.write(coded)

    def load_file(self):
        with open(self.filename, "r") as file:
            coded = file.read()
        self.nobles = json.loads(coded)

game = DictNobles()
    
while True:
    raw_action = input("What next? (New, Random new, Delete, View, View all, Exit)")
    action = raw_action.lower()
    if action == "exit":
        break
    elif action == "new":
        game.create_noble()
    elif action == "random new":
        game.create_random_noble()
    elif action == "delete":
        game.remove_noble()
    elif action == "view":
        game.get_stats()
    elif action == "view all":
        game.view_all()
    else:
        print("That's not a valid input, dumbass")
