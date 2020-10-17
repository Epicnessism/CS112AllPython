from Actions import DropLoot, Upgrade
from weaponDropRandomizer import getRandomizedStatsValues
from Attributes import ExistingAttributes

from utilsIO.loadData import readCharacterSaveFile
from CharacterModels.PlayerDAO import Player



playerInfoMap = readCharacterSaveFile("001.json") #map of player's info
player = Player(playerInfoMap)
consumedMaterials = {
    "bearFur_2": {
        "amount": 1
    }
}

myFirstWeapon = DropLoot.dropWeaponBase(player.level, getRandomizedStatsValues(player.level), [ExistingAttributes.freezeAttribute], consumedMaterials)

print(myFirstWeapon.stats)
# print(myFirstWeapon.getWeaponLevel())
# print(myFirstWeapon.weaponLevel)

Upgrade.upgradeWithMaterials(myFirstWeapon, "bearFur_1", 10)
print(myFirstWeapon.consumedMaterials)
print(myFirstWeapon.stats)

Upgrade.upgradeWithMaterials(myFirstWeapon, "bearFur_1", 1)
print(myFirstWeapon.consumedMaterials)
print(myFirstWeapon.stats)

Upgrade.upgradeWithMaterials(myFirstWeapon, "bearFur_1", 9)
print(myFirstWeapon.consumedMaterials)
print(myFirstWeapon.stats)

Upgrade.upgradeWithMaterials(myFirstWeapon, "wolfFang_1", 9)
print(myFirstWeapon.consumedMaterials)
print(myFirstWeapon.stats)