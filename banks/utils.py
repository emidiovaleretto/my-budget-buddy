def calculate_total(obj, field):
    total = 0
    for i in obj:
        total += getattr(i, field)

    return total