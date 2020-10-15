from GearDataObjectModels import WeaponBaseObject


def dropWeaponBase(playerLevel, statsValuesArray, attributeArray, consumedMaterials):
    weaponBase = WeaponBaseObject.WeaponBase(playerLevel, statsValuesArray, attributeArray, consumedMaterials)
    return weaponBase



