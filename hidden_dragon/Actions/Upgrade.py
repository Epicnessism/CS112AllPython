from Materials.MaterialDAO import Material
from utilsIO.loadData import readMaterialsFile

def upgradeWithMaterials(weapon, material):
    materialsJson = None
    if materialsJson is None:
        materialsJson = readMaterialsFile()
    print(materialsJson)
    print(materialsJson[material])

def upgradeWithForging():
    pass
