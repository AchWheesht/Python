class ConsoleView():
    def __init__(self):
        pass

    def display_commands(commands):
        print(commands)
    
    def display(self, status):
        for action, detail, plural in status:
            if action == "eat":
                if plural == False:
                    print("Gavin ate a %s" % (detail))
                elif plural == True:
                    print("Gavin ate some %s" % (detail))
                else:
                    raise ValueException("Plural?")
            elif action == "invalid":
                print("That is not a valid command! Gavin does nothing and grows slightly hungrier")
            elif action == "death":
                print("Gavin died. Because of %s. I hope you're happy" % (detail))
            else:
                raise ValueException("Unknown action")

    def goodbye(self):
        print("OH DEAR")
