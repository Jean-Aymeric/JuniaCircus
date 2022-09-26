from Artist import Artist

class Tamer(Artist):

    def __init__(self,name: str):
        Artist.__init__(self, name)

    def perform(self) -> str:
        return self.getName()+ ("ROAR ROAR MEOW MEOW GRRRR GRGRRRR")
