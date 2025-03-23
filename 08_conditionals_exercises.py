# Ejercicios de condicionales en python para principiantes.

# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
my_number = int(input("Introduce un número: "))

if my_number > 0:
    print("El número es positivo")
elif my_number < 0:
    print("El número es negativo")
else:
    print("El número es Cero")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
my_age = int(input("Cuantos años tienes: "))

if my_age < 18:
    print("Eres menor de edad")
elif my_age >= 18:
    print("Eres mayor de edad")

# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
my_text = input("Introduce un texto: ")

if not my_text:
    print("La cadena está vacía")
else:
    print("La cadena no está vacía")

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
num_user1 = int(input("Introduce el primer número: "))
num_user2 = int(input("Introduce el segundo número: "))

if num_user1 > num_user2:
    print(F"El número {num_user1} es mayor que {num_user2}")
elif num_user1 < num_user2:
    print(f"El número {num_user2} es mayor que {num_user1}")
else:
    print("Los dos números son iguales")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
division = int(input("Introduce el número a dividir: "))

if division % 3 == 0 and division % 5 == 0:
    print(f"El número {division} es divisible entre 3 y 5 al mismo tiempo")
else:
    print("El número no es divisible ni con el 3 ni con el 5 al mismo tiempo")

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
num_par = int(input("Ingresa un Número: "))

if num_par % 2 == 0:
    print(f"El número {num_par} es par.")
else:
    print(f"El número {num_par} es impar.")

# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
votante = int(input("Introduce tu edad para votar: "))

if votante >= 18:
    print("Puesdes Votar.")
elif votante >= 16:
    print("Puedes Votar con un Permiso Especial.")
else:
    print("No estás autorizado para votar.")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
password = "Python2025"
user_password = input("Introduce una contraseña: ")

if user_password == password:
    print("Acceso Permitido")
else:
    print("Error de contraseña.")
    
# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
numero = int(input("Ingresa un número: "))

if 10 <= numero <= 20:
    print(f"El número {numero} está entre 10 y 20.")
else:
    print(f"El número {numero} no está entre 10 y 20.")
 
# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
semaforo = input("Introduce un color (Rojo, Amarillo, Verde): ").lower()

if semaforo == "rojo":
    print("Detente")
elif semaforo == "amarillo":
    print("Precaución")
elif semaforo == "verde":
    print("Avanza")
else:
    print("Color no Válido")

# Final de los ejercicios de condicionales para principiantes en python.
