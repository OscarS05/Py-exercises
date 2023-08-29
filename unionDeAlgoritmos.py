def seleccionDeAlgoritmos ():
    opcion = int(input('¿Que algoritmo deseas utilizar para hallar la raíz cuadrada? Escoge el numero \n 1. enumeracionExhaustiva, \n 2. aproximacionDeSoluciones, \n 3. busquedaBinaria: '))
    objetivo = int(input('Escoge un numero: '))


    if opcion == 1:
        enumeracionExhaustiva(objetivo)
    elif opcion == 2:
        aproximacionDeSoluciones(objetivo)
    elif opcion == 3:
        busquedaBinaria(objetivo)
    else: 
        print('Elija 1,2 o 3')

def enumeracionExhaustiva (objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else: 
        print(f'{objetivo} no tiene una raíz cuadrada exacta')

def aproximacionDeSoluciones (objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    
    while abs(objetivo - respuesta**2) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(objetivo - respuesta**2) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
 
def busquedaBinaria (objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else: 
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raíz cuadrada de {objetivo} es {respuesta}')


seleccionDeAlgoritmos()