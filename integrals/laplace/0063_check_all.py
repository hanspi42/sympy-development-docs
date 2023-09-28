# -*- coding: utf-8 -*-
import sympy
from sympy import *
import sys
file_path = '0063_stderr.txt'
sys.stderr = open(file_path, "w")
sympy.SYMPY_DEBUG=True

LT = laplace_transform
ILT = inverse_laplace_transform
a, b, c, t = symbols('a, b, c, t', positive=True)
n = symbols('n', integer=True)
s, w, x, k = symbols('s, w, x, k')
f = Function('f')
F = Function('F')
g = Function('g')
y = Function('y')
Y = Function('Y')

# 129-133 (4.1)
# list_f = [
#     Heaviside(t-b/a) * f(a*t-b), exp(-a*t) * f(t), t**n*f(t), t**5*f(t),
#     t**(-n)*f(t), diff(f(t), t, n), diff(f(t), t, 5)]
# (4.2)
# list_f = [  # 1-8
#     1, (Heaviside(t-a)-Heaviside(t-b)), t**n, t**5, Heaviside(t-b)*t**n,
#     Heaviside(t-b)*t**5, Heaviside(-t+b)*t**n, Heaviside(-t+b)*t**5,
#     Heaviside(t-b)/(t+a), (Heaviside(t-c)-Heaviside(t-b))/(t+a), 1/(t-a)]
# list_f = [  # 9-16
#     1/(t+a)**2, 1/(t+a)**n, (b*t+c)/(t**2-a**2), Heaviside(t-b)/sqrt(t),
#     (1-Heaviside(t-b))/sqrt(t)
#     ]
# list_f = [  # 17-24
#     t**(n-S.Half), t**(4-S.Half), 1/(t+a), Heaviside(t-b)*(t)**(-S(3)/2),
#     (t+a)**(-S(3)/2), sqrt(t)/(t+a), Heaviside(t-b)*sqrt(t-b)/t,
#     (1+2*a*t)/sqrt(t)]
# list_f = [  # 25-32
    # 1/sqrt(t)/(t+a),  Heaviside(t-b)/sqrt(t-b)/t, t/sqrt(t**2+a**2),
    # Heaviside(b-t)*t/sqrt(b**2-t**2), Heaviside(t-b)*t/sqrt(t**2-b**2),
    # (t+a)/sqrt(t**2+2*a*t),
    # Heaviside(2*b-t)*sqrt(2*b*t-t**2)*(b-t), 1/(t+sqrt(t**2+a**2))
    # ]

for x in list_f:
    X = LT(k*x, t, s)
    print('\n', k*x, '\n', X, '\n', file=sys.stderr)