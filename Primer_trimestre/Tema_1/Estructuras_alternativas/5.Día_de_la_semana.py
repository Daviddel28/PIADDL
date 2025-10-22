n = int(input("Día (1=Lunes, ..., 7=Domingo): "))
dias = {
    1: "Lunes", 2: "Martes", 3: "Miércoles",
    4: "Jueves", 5: "Viernes", 6: "Sábado", 7: "Domingo"
}
print(dias.get(n, "Error: día inválido"))
