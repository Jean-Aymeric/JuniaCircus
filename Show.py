from Artist import Artist
from Performance import Performance

class Show:

    __date : str
    __hour : str
    __name : str
    __location: []
    __artist: [Artist]
    __performance: [Performance]

    def __init__(self,name: str, date : str, hour: str):
            self.__date = date
            self.__name = name
            self.__hour = hour
            self.__artist = []
            self.__performance = []

        def getName(self):
            return self.__name

        def getDate(self):
            return self.__date

        def getHour(self):
            return self.__hour

        def getLocation(self):
            return self.__location

        def addPerformance(self, performance: Performance):
            self.__performance.append(performance)

        def addArtist(self, artist: Artist):
            self.__artist.append(artist)
            #j'ai bcp trop taffer sur ce projet!!!  (qui peux me test?)