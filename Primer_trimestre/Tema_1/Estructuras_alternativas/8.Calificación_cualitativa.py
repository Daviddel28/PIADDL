nota = float(input("Nota numérica (0 a 10): "))

if nota == 10:
    print("Matrícula de Honor")
elif nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
