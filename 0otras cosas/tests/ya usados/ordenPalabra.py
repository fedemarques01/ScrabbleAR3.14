def lineal(coor, n):
    x = coor[0][n]
    for i in range(1, len(coor)):
        if(coor[i][n] != x):
            return False
    return True


def tieneOrden(coor):
    if(lineal(coor, 0)):
        return sorted(coor, key=lambda coor: coor[1])
    if(lineal(coor, 1)):
        return sorted(coor, key=lambda coor: coor[0])
    return []


c = [[0, 0], [2, 0], [1, 0], [3, 0]]
c = tieneOrden(c)
try:
    c[0]
    print(c)
except IndexError:
    print('ta mal')