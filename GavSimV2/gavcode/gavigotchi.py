from gavinmodel import GavinModel
from textcontroller import TextController
from consoleview import ConsoleView

gavin = GavinModel(10, 10, 10)
view = ConsoleView()
controller = TextController(gavin, view)

while True:
    controller.game_step()
