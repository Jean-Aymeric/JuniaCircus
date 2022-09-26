from Artist import Artist

class Acrobat(Artist):

    def __init__(self,name: str):
        Artist.__init__(self, name)

    def perform(self) -> str:
        return self.getname, ("VROUM VROUM LES ACROBATIES")
