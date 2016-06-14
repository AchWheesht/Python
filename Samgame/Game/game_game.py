#This is the main program which runs the game, importing the other files and starting the main
#controller function, and printing the death screen upon death (which is currently only possible via the "suicide" option in events)

import game_Controller
import game_Events
import game_Nobles
import game_Stats
import time

#Here we set up the class instances for the game

Nobles = game_Nobles.Noblesclass()
Stats = game_Stats.Statsclass()
Events = game_Events.Eventsclass()
Controller = game_Controller.Controllerclass()

#Next we run a function in stats to set up the starting stats. Doing it this way, rather than just setting up the stats
#when we create the class instance, allows for two things; First, we can load saved files for the stats. Second, we can set up stats
#that depend on other class instances - in this case a stat counting the number of nobles we have. In have to use a funciton to set this up,
#as I cannot refer to the Nobles instance when building the class

Stats.initialise_stats(Nobles, Stats, Events)
Nobles.initialise_nobles()

#Next, we tell controller to start collecting inputs. Currently, the main game loop is there - later, there will be periods where
#loops should occur without inputs (running a series of events, for example).

Controller.global_commands(Nobles, Stats, Events)

#If the player evver dies, the loops in controller  terminate and we get a death screen.

if Stats.is_alive == False:
    print("Game over, man, game over!")

while Stats.is_alive == False:
      time.sleep(3)
      print("YOU LOSE")
