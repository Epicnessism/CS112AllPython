import json


def readCharacterSaveFile(saveFile) -> json:
    with open('hidden_dragon/Saved Games/' + saveFile) as file:
        saveData = json.load(file)
    print(saveData)
    return saveData


def readMaterialsFile() -> json:
    with open('hidden_dragon/Materials/materials.json') as file:
        materialsData = json.load(file)
        print(materialsData)
        return materialsData
