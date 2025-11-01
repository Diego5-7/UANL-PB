import sympy as sp

x = sp.Symbol('x')

ecu1 = sp.Eq(x**2 - 5*x + 7, 0)
sol1 = sp.solve(ecu1)

ecu2 = sp.Eq(7*x**2 + 9*x - 7, 8*x**2 - 2*x - 3)
sol2 = sp.solve(ecu2)

print("a) Solución:", sol1)
print("b) Solución:", sol2)
