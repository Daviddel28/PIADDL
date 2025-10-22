import math

A = float(input("Lado A: "))
B = float(input("Lado B: "))
C = float(input("Lado C: "))

# Validación: deben poder formar triángulo
if A <= 0 or B <= 0 or C <= 0 or A + B <= C or A + C <= B or B + C <= A:
    print("No forman un triángulo válido.")
else:
    x, y, z = sorted([A, B, C])  # z es el mayor
    if math.isclose(z*z, x*x + y*y, rel_tol=1e-9, abs_tol=1e-12):
        print("Triángulo rectángulo")
    elif math.isclose(A, B) and math.isclose(B, C):
        print("Triángulo equilátero")
    elif math.isclose(A, B) or math.isclose(A, C) or math.isclose(B, C):
        print("Triángulo isósceles")
    else:
        print("Triángulo escaleno")
