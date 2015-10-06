class TextController():
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def game_step(self):
        command = str.lower(input("Input command\n"))
        gav_commands = {
            "eat": self.gavin_eat,
            "eat_steak": self.gavin_eat_steak,
            "eat_carrot": self.gavin_eat_carrot,
            "eat_nitro": self.gavin_eat_nitro,
            "quit": self.abort_abort_abort,
            "help": self.display_commands(gav_commands) #this is the command I'm having trouble with
            }
        method = gav_commands.get(command, self.gavin_invalid_command)
        method()

    def display_commands(self, gav_commands): #this is the function to display commands
        command_list = gav_commands.items() #it returns the error "local variable 'gav_commands' referenced before assignment"
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

    def consequences(self, status):
        died = filter(lambda message: message[0] == "death", status)
        self.view.display(status)
        if list(died):
            self.abort_abort_abort()

    def abort_abort_abort(self):
        self.view.goodbye()
        exit()
    
