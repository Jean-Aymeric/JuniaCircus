from Performance import Performance

class Artist:
    __name: str
    __performances: Performance
    __teams : []

    def __init__(self, name: str, performance: Performance):
        self.__name = name
        self.__performances = []
        self.__teams = []

    def getName(self) -> str :
        return(self.__name)

    def perform(self) -> str :
        return (self.__performances)

    def addPerformance(self, performance: Performance):
        if performance not in self.__performances:
            self.__performances.append(performance)
            performance.addArtist(self)

    def addTeam(self, team):
        if team not in self.__teams :
            self.teams.append(team)
            team.addArtist(self)

