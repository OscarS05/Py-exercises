nombre_usuario1 = input('¿Cuál es tu nombre?: ')
nombre_usuario2 = input('¿Cuál es tu nombre?: ')

edad_1 = int(input(f'¿Cuál es tu edad {nombre_usuario1}?: '))
edad_2= int(input(f'¿Cuál es tu edad {nombre_usuario2}?: '))

if edad_1 > edad_2:
    print(f'La edad de {nombre_usuario1} es mayor que la de {nombre_usuario2}')
elif edad_1 < edad_2:
    print(f'La edad de {nombre_usuario2} es mayor que la de {nombre_usuario1}')
else:
    print(f'Las edad de {nombre_usuario1} y la edad de {nombre_usuario2} son iguales')