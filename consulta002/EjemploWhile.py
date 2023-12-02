suma = 0
print("---------------------------Suma de secuencias-----------------------------")
print("Ingrese un numero al cual se desee iniciar la suma de secuencias")
secuencia1 = int(input())
print("Ingrese el número al cual se desee teminar la suma de secuencias")
secuencia2 = int(input())
while (secuencia1 <= secuencia2):
    suma = secuencia1 + suma
    secuencia1 = secuencia1 + 1

print("--------------------------------------------------------------------------")
print(suma)