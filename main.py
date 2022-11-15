import sympy
from matplotlib import*
import numpy as np
from sympy.plotting import plot
from sympy import symbols

#График
x = symbols('x')
func = -12*x**4*sympy.sin(sympy.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
plot(func,(x,-100,100), title = 'График функции')

print(f'Точка пересечения с осью Y: [0 ,{func.subs(x, 0)}]')
print(f'Функция f(x) = {func}, имеет бесконечное число корней и не имеет экстремумов')

print(f'Производная 1-го порядка: {func.diff(x)}')

derivativeOfFunc = func.diff(x)
print('На участках где: \n(derivativeOfFunc < 0) - функция убывает \n(derivativeOfFunc > 0) - функция возрастает')
plot(func,(x,-10,10),line_color='red',title='График func(x)')
plot(derivativeOfFunc,(x,-10,10),line_color='blue',title='График derivativeOfFunc(x)')

