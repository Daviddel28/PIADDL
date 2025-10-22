n = int(input("Número de dos cifras: "))
decenas = n // 10
unidades = n % 10
invertido = unidades * 10 + decenas
print("Invertido:", invertido)

