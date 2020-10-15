

class Player:
    def __init__(self, playerInfoMap):
        self.name = playerInfoMap["playerInfo"]["name"]
        self.level = playerInfoMap["playerInfo"]["level"]
        self.health = playerInfoMap["playerInfo"]["health"]
        self.inventory = playerInfoMap["playerInfo"]["inventory"]
        self.location = playerInfoMap["playerInfo"]["location"]




