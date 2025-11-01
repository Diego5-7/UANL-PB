import numpy as np
from scipy.integrate import quad

def f(x):
    return np.sin(x**2)

resultado, error = quad(f, 0, 2)

print("Integral de sin(x^2) en [0,2]:", round(resultado, 5))
