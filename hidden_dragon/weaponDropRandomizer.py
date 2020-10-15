import math
import random

# numberOfAttributes = 20
numberOfAttributes = 12


def getRandomizedStatsValues(playerLevel):
    # random.seed() #not sure if needed
    lvlModifier = math.floor(playerLevel / numberOfAttributes) + 1  # each 20 levels the amount of points for a starting weapon is multiplied by this modifier

    # totalPointsToDistribute = 20 * lvlModifier
    totalPointsToDistribute = numberOfAttributes * lvlModifier  # temp values

    attributeValuesList = []
    while totalPointsToDistribute > 0:
        for x in range(numberOfAttributes):
            randomStatValue = random.randint(0, lvlModifier)
            if randomStatValue <= totalPointsToDistribute & totalPointsToDistribute != 0 & randomStatValue >= 0:
                totalPointsToDistribute -= randomStatValue
            else:
                break
            if len(attributeValuesList) < numberOfAttributes:
                attributeValuesList.append(randomStatValue)
            else:
                attributeValuesList[x] += randomStatValue

    random.shuffle(attributeValuesList)
    checkTotalValueCount(attributeValuesList)
    return attributeValuesList


def checkTotalValueCount(attributeValueList) -> int:
    sum = 0
    for x in attributeValueList:
        sum += x
    print(sum)
    return sum
