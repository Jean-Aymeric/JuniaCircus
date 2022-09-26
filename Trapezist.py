from Artist import Artist

class Trapezist(Artist):

    def __init__(self,name: str):
        Artist.__init__(self, name)

    def perform(self) -> str:
        return self.getName()+ ("JE FAIS DU TRAPEZE LEEEET'S GOOO")
