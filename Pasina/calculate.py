import math
import random

#проверка корректности входных данных
def calculate_material(product_type_id, material_type_id, quantity, param1, param2):
    if not all(isinstance(x, (int, float)) for x in [product_type_id, material_type_id, quantity, param1, param2]):
        return -1
    if quantity <= 0 or param1 <= 0 or param2 <= 0:
        return -1

    product_coefficent = {1: 1.5, 2: 2.0} # коэффиценты для типов продуктов
    material_defect_rates = {1: 0.1, 2: 0.2} # процент брака для типов материала

    if product_type_id not in product_coefficent or material_type_id not in material_defect_rates:
        return -1

    # общий расчет материала на единицу продукции
    product_coefficent = product_coefficent[product_type_id]
    material_per_unit = param1 * param2 * product_coefficent

    # учет процента брака
    defect_rate = material_defect_rates[material_type_id]
    total_material = material_per_unit * quantity / (1 - defect_rate)

    return math.ceil(total_material) # округление до целого


def calculate_discount(total_qunatity):
    if total_qunatity < 10000:
        return 0
    elif 10000 <= total_qunatity < 50000:
        return 5
    elif 50000 <= total_qunatity < 300000:
        return 10
    else:
        return 15

