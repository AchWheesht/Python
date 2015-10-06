class TextController():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.gav_commands = {
            "eat": self.gavin_eat,
            "eat steak": self.gavin_eat_steak,
            "eat carrot": self.gavin_eat_carrot,
            "eat nitro": self.gavin_eat_nitro,
            "quit": self.abort_abort_abort,
            "help": self.display_commands
            }

    def game_step(self):
        command = str.lower(input("Input command\n"))
        method = self.gav_commands.get(command, self.gavin_invalid_command)
        method()

    def display_commands(self):
        command_list = list(self.gav_commands.keys())
        command_list.sort()
        self.view.display_commands(command_list)

    def gavin_eat(self):
        self.consequences(self.model.eat())

    def gavin_eat_steak(self):
        self.consequences(self.model.eat_steak())

    def gavin_eat_carrot(self):
        self.consequences(self.model.eat_carrot())

    def gavin_eat_nitro(self):
        self.consequences(self.model.eat_nitro())

    def gavin_invalid_command(self):
        self.consequences(self.model.invalid_command())

    #trying to fully understand what this does. does it remove "death"
    #from the list? It shouldn't, but the display function in consoleview
    #still works regardless. Can you enlighten me?

    def consequences(self, status):
        died = filter(lambda message: message[0] == "death", status)
        self.view.display(status)
        if list(died):
            self.abort_abort_abort()

    def abort_abort_abort(self):
        self.view.goodbye()
        exit()
    
