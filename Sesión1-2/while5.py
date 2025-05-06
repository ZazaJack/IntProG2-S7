cadena = input("Introduce una cadena: ")

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for caracter in cadena.lower():  
    if caracter == 'a':
        contador_a += 1
    elif caracter == 'e':
        contador_e += 1
    elif caracter == 'i':
        contador_i += 1
    elif caracter == 'o':
        contador_o += 1
    elif caracter == 'u':
        contador_u += 1

print(f"Vocal 'a': {contador_a}")
print(f"Vocal 'e': {contador_e}")
print(f"Vocal 'i': {contador_i}")
print(f"Vocal 'o': {contador_o}")
print(f"Vocal 'u': {contador_u}")

total_vocales = contador_a + contador_e + contador_i + contador_o + contador_u
print(f"Total de vocales: {total_vocales}")