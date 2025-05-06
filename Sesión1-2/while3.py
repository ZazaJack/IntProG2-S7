N = int(input("Introduce un número entero positivo: "))

if N <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    
    suma = 0
    
    for i in range(1, N + 1):
        suma += i  
        
    print(f"La suma de los primeros {N} números es: {suma}")