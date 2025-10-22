cantidad = int(input("Cantidad exacta en euros: "))
resto = cantidad
denominaciones = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for d in denominaciones:
    num, resto = divmod(resto, d)
    if num:
        tipo = "billete" if d >= 5 else "moneda"
        print(f"{num} {tipo}(s) de {d}€")
