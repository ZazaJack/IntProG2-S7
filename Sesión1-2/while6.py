N = int(input("Introduce la cantidad de calificaciones: "))

if N <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    suma_calificaciones = 0  
    
    for i in range(N):
        calificacion = float(input(f"Introduce la calificación {i + 1}: "))  
        suma_calificaciones += calificacion  
    
    promedio = suma_calificaciones / N
    
    print(f"El promedio de las calificaciones es: {promedio:.2f}")
