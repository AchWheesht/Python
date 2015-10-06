class ConsoleView():
    def __init__(self):
        pass

    def display_commands(self, commands):
        print("Here are the current commands you can use")
        print(commands)

#I have been tinkering with the consoleview. Currently, I'm assigning a personalised
#message for each action, rather than building the messages. I would like to be able to print
#personlised death messages, but I'm unsure how to utlise the obit value in the data that is
#passed to display. I'm pretty sure obit gets passed along to here detail, though not 100% sure.
#check textcontroller for details on that.
    
    def display(self, status):
        for action, detail in status:
            if action == "eat":
                if detail == "steak":
                    print("Gavin ate a steak. It tasted good! Gavin feels guilty")
                elif detail == "carrot":
                    print("Gavin ate a carrot. It tasted good! It wasn't very filling.")
                elif detail == "nitroglycerine":
                    print("Gavin ate some nitroglycerine. It didn't taste good! It wasn't very filling. The nitroglycerine explodes! Gavin is hurt!")
                else:
                    raise ValueException("Food not recognised. Check model.")
            elif action == "invalid":
                print("That is not a valid command! Gavin does nothing and grows slightly hungrier")
            elif action == "death":
                print("Gavin died. Because of %s. I hope you're happy" % (detail))
                print(obit) #Can you suggest a way to make this work?
            else:
                raise ValueException("Unknown action")

    def goodbye(self):
        print("OH DEAR")
