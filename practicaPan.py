barras = int(input("\nIntroduce el número de barras de pan vendidas que no son frescas:\n\t "))
precio = 27 
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es:\n\t $" + str(precio))
print("El descuento sobre una barra no fresca es: \n\t" + str(descuento * 100) + "%")
print("El coste final a pagar es:\n\t $" + str(round(coste, 2)))