from random import choice

class GavinModel():
    def __init__(self, health, hunger, happiness):
        self.health = health
        self.hunger = hunger
        self.happiness = happiness

    def invalid_command(self):
        """This function runs when an invalid command is entered"""
        self.hunger = self.hunger - 2
        return self.status(("invalid", None, None))

    def eat(self):
        eat_methods = [self.eat_steak, self.eat_carrot, self.eat_nitro]
        event = choice(eat_methods)
        return event()

    def eat_steak(self):
        """This function has gavin eat a steak"""
        self.hunger = self.hunger + 5
        self.happiness = self.happiness - 5
        return self.status(("eat", "steak"))

    def eat_carrot(self):
        """This function has gavin eat a carrot"""
        self.health = self.health + 1
        self.hunger = self.hunger + 1
        self.happiness = self.happiness + 1
        return self.status(("eat", "carrot"))

    def eat_nitro(self):
        """This function has gavin eat nitroglycerine"""
        self.health = self.health - 8
        return self.status(("eat", "nitroglycerine"))

    def status(self, message):
        state = [message]
        obit = self.is_dead()
        if obit:
            state.append(("death", obit))
        return state

    def is_dead(self):
        """This function checks if gavin is alive"""
        if self.health <= 0:
            return "health"
        elif self.hunger <= 0:
            return "hunger"
        elif self.happiness <= 0:
            return "happiness"
        else:
            return None
