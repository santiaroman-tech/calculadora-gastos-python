def calcular_total(gasto1, gasto2, gasto3):
    """Calcula y retorna la suma de tres gastos."""
    return gasto1 + gasto2 + gasto3


def calcular_promedio(total_gastos, cantidad_gastos):
    """Calcula y retorna el promedio de los gastos realizados."""
    if cantidad_gastos == 0:
        return 0
    return total_gastos / cantidad_gastos


def clasificar_gasto(total_gastos):
    """Clasifica el nivel de gasto según el monto total."""
    if total_gastos <= 5000:
        return "Gasto bajo"
    elif total_gastos <= 10000:
        return "Gasto moderado"
    else:
        return "Gasto elevado"
