mayor = None
for i in range(5):
    n = int(input(f"Número {i+1}: "))
    if mayor is None or n > mayor:
        mayor = n

print("El mayor es:", mayor)
