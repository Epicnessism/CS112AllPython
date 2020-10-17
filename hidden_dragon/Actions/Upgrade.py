import math

from Materials.MaterialDAO import Material
from utilsIO.loadData import readMaterialsFile

def upgradeWithMaterials(weapon, materialID, materialAmount):
    materialsJson = None
    if materialsJson is None:
        materialsJson = readMaterialsFile()
    # print(materialsJson)
    # print(materialsJson[materialID])
    material = materialsJson[materialID]
    # print(material)
    # print(weapon.consumedMaterials)
    if materialID not in weapon.consumedMaterials:
        weapon.consumedMaterials[materialID] = {}
        weapon.consumedMaterials[materialID]["amount"] = 0

    upgradeForEachPositiveStat(weapon, material, materialAmount, materialID)


def upgradeWithForging():
    pass


def upgradeForEachPositiveStat(weapon, material, materialAmount, materialID):

    for positiveStat in material["augments"]["positive"]:
        materialAmountLocal = materialAmount
        while materialAmountLocal > 0:
            # print(positiveStat)
            matsConsumed = weapon.consumedMaterials[materialID]["amount"]  # amount of invested mats
            matsPerPoint = positiveStat["amountPerPoint"]

            pointsApplied = math.floor(matsConsumed / matsPerPoint)
            amountMatsNextPoint = (pointsApplied + 1) * matsPerPoint
            matsUntilNextPoint = amountMatsNextPoint - matsConsumed

            # print("matsUntilNextPoint" + str(matsUntilNextPoint))
            # print("materialAmountLocal" + str(materialAmountLocal))
            if matsUntilNextPoint <= materialAmountLocal:
                materialAmountLocal -= matsUntilNextPoint
                weapon.stats[positiveStat["stat"]] += 1
            else:
                materialAmountLocal = 0

    for negativeStat in material["augments"]["negative"]:
        materialAmountLocal = materialAmount
        while materialAmountLocal > 0:
            # print(negativeStat)
            matsConsumed = weapon.consumedMaterials[materialID]["amount"]  # amount of invested mats
            matsPerPoint = negativeStat["amountPerPoint"]

            pointsApplied = math.floor(matsConsumed / matsPerPoint)
            amountMatsNextPoint = (pointsApplied + 1) * matsPerPoint
            matsUntilNextPoint = amountMatsNextPoint - matsConsumed

            # print("matsUntilNextPoint" + str(matsUntilNextPoint))
            # print("materialAmountLocal" + str(materialAmountLocal))
            if matsUntilNextPoint <= materialAmountLocal:
                materialAmountLocal -= matsUntilNextPoint
                if weapon.stats[negativeStat["stat"]] > 0:
                    weapon.stats[negativeStat["stat"]] -= 1
            else:
                materialAmountLocal = 0

    weapon.consumedMaterials[materialID]["amount"] += materialAmount

