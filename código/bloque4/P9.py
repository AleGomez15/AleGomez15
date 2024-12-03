#Programa 9 
#Alejandra Guadalupe Gomez Cruz
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1 # Equivalente a i = i + 1 
print("Fin del programa")

# Ejemplo 2 - continue 
# Imprimir los números del 1 al 10, pero si el número es 5 evitarlo 
i = 1 
while i <= 10 :
    if i == 5:
        i += 1
        continue 
    print(i)
    i += 1
print("Fin del programa")
