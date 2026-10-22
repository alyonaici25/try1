import math 
first_side_lenght = float(input("Введите длину первой стороны треугольника: "))
second_side_lenght = float(input("Введите длину второй стороны треугольника: "))
angle = float(input("Задайте угол между ними в градусах: "))
third_side_lenght = first_side_lenght**2 + second_side_lenght**2 - 2 * first_side_lenght * second_side_lenght * math.cos(math.radians(angle)) 

print("Длина третьей стороны треугольника: ", third_side_lenght)
print("Well done!")
