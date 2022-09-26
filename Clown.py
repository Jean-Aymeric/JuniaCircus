from Artist import Artist

class Clown(Artist):

    def __init__(self,name: str):
        Artist.__init__(self, name)

    def perform(self) -> str:
        return self.getName()+ ("JE SUIS UN CLOWN OUGA OUGA LE CLOWN DROLE")