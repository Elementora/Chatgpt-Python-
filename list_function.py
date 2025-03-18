# Bir listede tüm sayıların karesini alan bir fonksiyon

def kareler(lst):
    return [x ** 2 for x in lst]


print(kareler([1, 2, 3, 4,]))

# Bir listede tüm sayıların küpünü alan bir fonksiyon


def küpler(lst):
    return [x ** 3 for x in lst]


print(küpler([1, 2, 3, 4,]))
