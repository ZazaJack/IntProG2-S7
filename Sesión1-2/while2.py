print("Escribe palabras y al final escribe 'fin' para terminar")

for palabra in iter(input, "fin"):
    print(f"{palabra.capitalize()} tiene {len(palabra)} letras")
else:
    print("Fin del programa")
    