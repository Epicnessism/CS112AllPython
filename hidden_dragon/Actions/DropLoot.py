from GearDataObjectModels import WeaponBaseObject


def dropWeaponBase(playerLevel, statsValuesArray, attributeArray):
    weaponBase = WeaponBaseObject.WeaponBase(playerLevel, statsValuesArray, attributeArray)
    return weaponBase