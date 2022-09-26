from Artist import Artist

class Ringmaster(Artist):

    def __init__(self,name: str):
        Artist.__init__(self, name)

    def perform(self) -> str:
        return self.getName()+ ("SALUT A TOUTES ET A TOUS ON VA FAIRE DU CIRQUE")


