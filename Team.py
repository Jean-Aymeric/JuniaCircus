from Artist import Artist

class Team:
    __name : str
    __artists : []

    def __init__(self, name: str):
        self.__name = name
        self.__artists = []

    def getName(self) -> str :
        return(self.__name)

    def addArtist(self, __artist : Artist):
        self.__artist.append(Artist)