class BuildingError(Exception):
    def __str__(self):
        return f'with this amount of material we can`t build this house'
def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return 'enough material'
    else:
        raise BuildingError(amount_of_material)
material = 123
check_material(material, 300)
