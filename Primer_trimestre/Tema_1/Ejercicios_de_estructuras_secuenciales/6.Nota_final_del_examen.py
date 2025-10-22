P_CORRECTA   = 5
P_INCORRECTA = -1
P_BLANCA     = 0

c = int(input("Respuestas correctas: "))
i = int(input("Respuestas incorrectas: "))
b = int(input("Respuestas en blanco: "))

total = c*P_CORRECTA + i*P_INCORRECTA + b*P_BLANCA
num_preguntas = c + i + b

if num_preguntas == 0:
    print("No hay preguntas evaluadas.")
else:
    # Normaliza a 0–10 asumiendo que la máxima puntuación es num_preguntas * P_CORRECTA
    nota_0a10 = (total / (num_preguntas * P_CORRECTA)) * 10
    # Limita a [0,10] por si el total cae fuera de rango
    nota_0a10 = max(0, min(10, nota_0a10))
    print(f"Puntuación total: {total}")
    print(f"Nota (0–10): {nota_0a10:.2f}")
