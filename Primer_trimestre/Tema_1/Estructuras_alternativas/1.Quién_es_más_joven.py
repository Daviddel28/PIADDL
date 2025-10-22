edad1 = int(input("Edad de la primera persona: "))
edad2 = int(input("Edad de la segunda persona: "))

if edad1 < edad2:
    print("La primera persona es más joven.")
elif edad2 < edad1:
    print("La segunda persona es más joven.")
else:
    print("Tienen la misma edad.")
    