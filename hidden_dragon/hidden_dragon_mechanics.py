from Actions import DropLoot
from weaponDropRandomizer import getRandomizedStatsValues
from Attributes.ExistingAttributes import burnAttribute, freezeAttribute

from utilsIO.loadData import readCharacterSaveFile
from CharacterModels.PlayerDAO import Player

playerInfoMap = readCharacterSaveFile("001.json") #map of player's info
player = Player(playerInfoMap)


myFirstWeapon = DropLoot.dropWeaponBase(player.level, getRandomizedStatsValues(player.level), [freezeAttribute])

print(myFirstWeapon.stats)
print(myFirstWeapon.attributes)

