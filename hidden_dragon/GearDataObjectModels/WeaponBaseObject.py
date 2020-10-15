class WeaponBase:
    def __init__(self, weaponLevel, statsValuesArray, attributesArray, consumedMaterials):
        print(statsValuesArray)
        # self.__weaponLevel = weaponLevel
        self.weaponLevel = weaponLevel
        self.stats = {
            "attack": statsValuesArray[0],
            "health": statsValuesArray[1],
            "defense": statsValuesArray[2],
            "agility": statsValuesArray[3],
            "criticalChance": statsValuesArray[4],
            "criticalDamage": statsValuesArray[5],
            "effectResist": statsValuesArray[6],
            "effectiveness": statsValuesArray[7],
            "weight": statsValuesArray[8],
            "durability": statsValuesArray[9],
            "Hardness": statsValuesArray[10],
            "range": statsValuesArray[11],
        }
        self.attributes = attributesArray
        self.consumedMaterials = consumedMaterials

    def getWeaponLevel(self):
        print("Weapon Level: " + str(self.weaponLevel))

