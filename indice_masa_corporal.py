#definición de las variables
peso = float(input("Tu peso en Kilogramos es de: "))
estatura = float(input("Tu estatura en metros es de: "))

#cálculo del IMC
indice_de_masa_corporal = peso / (estatura**2)
resultado= round(indice_de_masa_corporal,2)

#resultado
print(f'Tu indice de masa corporal (IMC) es de {resultado}.')