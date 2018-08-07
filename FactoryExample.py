class Game(object):
    def factory(type):
        if type == "Action": return Action() 
        if type == "Shooter": return Shooter()
    factory = staticmethod(factory)

class Action(Game):
    def play(self): print("Playing an action game")

class Shooter(Game):
    def play(self): print("Playing a shooter game")

obj = Game.factory("Action")
obj.play()

obj2 = Game.factory("Shooter")
obj2.play()
