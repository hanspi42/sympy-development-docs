# -*- coding: utf-8 -*-
import sympy
from sympy import *
import sys
file_path = '0063_stderr.txt'
sys.stderr = open(file_path, "w")
sympy.SYMPY_DEBUG=True

LT = laplace_transform
ILT = inverse_laplace_transform
a, b, c = symbols('a, b, c', positive=True)
t = symbols('t', real=True)
n = symbols('n', integer=True)
np = symbols('np', integer=True, positive=True)
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
# (4.3)
# list_f = [  # 1-8
#     t**c, Heaviside(t-b)*t**c, Heaviside(b-t)*t**c, (t+a)**c,
#     Heaviside(t-b)*(t-b)**c, Heaviside(b-t)*(b-t)**c, t**c/(t+a),
#     Heaviside(t-b)*(t-b)**c/t]
# (Heaviside and t**np change)
# list_f = [
#     Heaviside(t-a)*g(t), Heaviside(t+a)*g(t), Heaviside(-t+a)*g(t),
#     Heaviside(-t-a)*g(t)]
# list_f = [t**n*g(t), t**np*g(t), t**5*g(t)]
# (4.4)
# list_f = [
#     Piecewise((t, Lt(t, 1)), (1, True)),
#     Piecewise((t, Lt(t, 1)), (t-2, Lt(t, 2)), (0, True)),
#     Piecewise((t**2/2, Lt(t, 1)), (1-(t-2)**2/2, Lt(t, 2)), (1, True)),
#     Piecewise((t**2/2, Lt(t, 1)), (S(3)/4-(t-S(3)/2)**2, Lt(t, 2)),
#               ((t-3)**2/2, Lt(t, 3)), (0, True))]
# (4.5)
# list_f = [  # 1-8
#     exp(-a*t), t*exp(-a*t), t**b*exp(-a*t),
#     (exp(-a*t)-exp(-b*t))/t, (1-exp(-a*t))**2/t**2,
#     1/t - (t+2)*(1-exp(-t))/(1*t**2), 1/(1+exp(-t)),
#     (1-exp(-t/a))**(b-1)]
# (4.6)
list_f = [
    # Heaviside(t-b)*exp(-t**2/4/a), t*exp(-t**2/4/a),
    # exp(-t**2/4/a)/sqrt(t), t**b*t*exp(-t**2/4/a),
    # exp(-a/(4*t)), sqrt(t)*exp(-a/(4*t)),
    # exp(-a/(4*t))/sqrt(t), exp(-a/(4*t))*t**(-S(3)/2),
    # exp(-a/(4*t))*t**(b-1), (exp(-a/(4*t)-1))/sqrt(t),
    # exp(-2*sqrt(a*t)), sqrt(t)*exp(-2*sqrt(a*t)),
    # exp(-2*sqrt(a*t))/sqrt(t), exp(-2*sqrt(a*t))/(2*t)**(S(3)/4), 
    # exp(-2*sqrt(a*t))*(2*t)**(b-1), exp(-a*exp(-t)),
    # exp(-a*exp(-t)), (1-exp(-t))**b-1*exp(a*exp(-t)),
    exp(-a*exp(-t)), exp(-a*exp(t)),
    ]

for x in list_f:
    X = LT(k*x, t, s)
    print('\n', k*x, '\n', X, '\n', file=sys.stderr)
    print(x)
    print(X[0].simplify())
    print(X, '\n')