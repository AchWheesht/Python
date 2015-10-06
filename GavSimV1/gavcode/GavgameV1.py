class Stats():
  """For objects which need to be assigned stats"""
  def __init__(self, health, hunger, sanity): #Initialising, setthing three main stats for gavin
    self.health = health
    self.hunger = hunger
    self.sanity = sanity

  def print_stats(self):
    """This Event prints current stats"""
    print ("Health:", self.health)
    print ("Hunger:", self.hunger)
    print ("Sanity:", self.sanity)

  def hunger_event(self):
    """This event refills hunger and harms sanity"""
    self.hunger = self.hunger + 3 #Increase hunger stat
    self.sanity = self.sanity - 5 #Decrease sanity stat
    print ("Gavin eats a steak. It tastes good, but it makes him feel guilty")
    print ("Hunger: +3. Current Hunger:", self.hunger)
    print ("Sanity: -5. Current Sanity:", self.sanity)
    
  def health_event(self):
    """This event heals gavin, but hurts his hunger"""
    self.health = self.health + 3
    self.hunger = self.hunger - 5
    print ("Gavin bandages his wounds with food. He feels better, but all the food makes him hungry")
    print ("Health: +3. Current Health:", self.health)
    print ("Hunger: -5. Current Hunger:", self.hunger)
    
  def sanity_event(self):
    """This event makes gavin saner, but hurts his body"""
    self.sanity = self.sanity + 3
    self.health = self.health - 5
    print ("Gavin sleeps. He feels better mentally, but a bear mauling in the night has left him several pints of blood down")
    print ("Sanity + 3. Current Sanity:", self.sanity)
    print ("Health: -5. Current Health:", self.health)
    
  def pass_event(self):
    """This event occurs when no valid input is found"""
    self.hunger = self.hunger - 1
    print ("That isn't a valid command! Gavin does nothing for a bit, and grows slightly hungrier""")
    print ("Hunger - 1. Current Hunger:", self.hunger)
    
  def is_alive(self):
    """This function checks whether gavin is alive"""
    if self.health <= 0:
      return False
    elif self.hunger <= 0:
      return False
    elif self.sanity <= 0:
      return False
    else:
      return True

gavin = Stats(10, 10, 10) #Creates an instance of "Gavin"

events = { #This dictioary is used to store event commands 
  "Eat": gavin.hunger_event,
  "Heal": gavin.health_event,
  "Sleep": gavin.sanity_event,
  "Stats": gavin.print_stats}

check_alive = gavin.is_alive()

while check_alive == True:
  user_command = input("Input Command: Eat, Heal, Sleep or Stats:\n") #Input command here
  if user_command in events: #Checks commands dictionary for match for raw input
    gavin_event = events[user_command]
    gavin_event()
  else:
    gavin.pass_event()
    
  check_alive = gavin.is_alive()
  
print (gavin.health, gavin.hunger, gavin.sanity)

print ("Gavin is dead. Game over")
