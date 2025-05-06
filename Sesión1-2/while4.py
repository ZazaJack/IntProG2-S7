M = int(input("Introduce un número entero positivo: "))
if M <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    producto = 1  
    contador = 0 
    numero = 2    
    while contador < M:
        producto *= numero  
        numero += 2         
        contador += 1       
    print(f"El producto de los primeros {M} números pares es: {producto}")