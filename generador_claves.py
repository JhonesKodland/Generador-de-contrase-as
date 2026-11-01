import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Introduce la longitud de la clave: "))
password = ""

# Generar la contraseña con un bucle for
for i in range(longitud):   
    password += random.choice(caracteres)

print(password)