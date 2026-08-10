# i need a game object
# a move function
# and 2 room objects

class NewGame:
    def __init__(self):
        self.name = input("Enter your name")
        self.current_room = start
        self.running = True
        #dunno

class Room:
    def __init__(self):
        self.name = name
        self.description = description
        self.connections = {}
        self.visited = False
        self.items = []
        #whatevs
    def enter(self):
        if not self.visited:
            print(self.description)
            self.visited = True
        else:
            print(f"Gecko crawls to the {self.name}")

start = Room("big rock", "the Gecko is chilling on a big rock") #see if this causes any issues
forest = Room("forest", "Gecko wanders in a damp forest")

start.connections["d"]=forest
forest.connections["u"]=start

game = NewGame()
start.enter()

def process_command():
    direction = input("> ")
    if direction in game.current_room.connections:
        game.current_room = game.current_room.connections[direction]
        game.current_room.enter()
    elif direction == "quit":
        game.running = False
    else:
        print("this is beyond our scope")

while game.running:
    process_command()