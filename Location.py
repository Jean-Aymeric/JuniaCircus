class Location:
import Show from Show

    __name : str
    __shows : [Show]

    def __init__(self, name: str) :
        self.__name = name
        self.__shows:[]


    def getName(self) -> str:
        return self.__name


    def addShows(self, show:Show ):
        if show not in self.__shows:
            self.__shows.append(show)
            show.addLocation(self)