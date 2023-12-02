print("--------Operaciones Aritmeticas Simples------------")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
print("Digite un numero del 1 al 4 segun la operacion que desea realizar")
print("1. Suma \n2. Resta \n3. Multiplicación \n4. Division")
numero = int(input())

if numero == 1:
    res = numero1 + numero2
    print("La suma es: ", res)
elif numero == 2:
    res = numero1 - numero2
    print("La resta es: ", res)
elif numero == 3:
    res = numero1 * numero2
    print("La multiplicación es: ", res)
elif numero == 4:
    res = numero1 / numero2
    print("La división es: ", res)
else:
    print("Error, usted debe ingresar un número del 1 al 4 segun la operación que desea realizar")
    