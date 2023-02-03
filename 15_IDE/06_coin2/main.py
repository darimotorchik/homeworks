import math


def find_a_coin(x, y, r):
    coin_radius = math.sqrt((x ** 2) + (y ** 2))
    coin_circumference = 2 * math.pi * coin_radius
    metal_detector_circumference = 2 * math.pi * r
    if coin_circumference <= metal_detector_circumference:
        return True
    return False


print('Введите координаты монетки:')
X = float(input('X: '))
Y = float(input('Y: '))
detector_radius = int(input('Введите радиус: '))

while detector_radius <= 0:
    detector_radius = int(input('Некорректный ввод! Значение радиуса должно быть больше 0\nПопробуйте еще раз: '))

if find_a_coin(X, Y, detector_radius):
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')
