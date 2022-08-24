# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda

import PySimpleGUI as sg

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro
    # potencia_2 = lambda x:......
    # pot_3 = potencia_2(3)

    potencia_2 = lambda x: 2**x
    pot_3 = potencia_2(3)
    print("La potencia de 2 al cubo es : ",pot_3)
 
    sg.theme('DarkPurple')
    layout = [[sg.Text('Potencia de 2 al cubo')],
    [sg.InputText(pot_3)],
    [sg.OK(), sg.Cancel ()]]

    window = sg.Window ('Ejercicio N° 1', layout)
    while True:
     event, values = window.read()
     if event in (sg.WIN_CLOSED, 'Cancel') :
        break
     window.close()
    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "potencia_2" dentro del map, debe colocar
    # directamente la lambda.

    # Lista de numeros
    numeros = [1, -5, 4, 3]

    # numeros_potencia = list(map....)
    numeros_potencia = list(map(lambda x: 2**x, numeros))
    print(numeros_potencia) 
    print("terminamos")
    
    sg.theme('DarkPurple')
    layout = [[sg.Text('La potencia de la lista = [1, -5, 4, 3] son :')],
    [sg.InputText(numeros_potencia)],
    [sg.OK(), sg.Cancel ()]]

    window = sg.Window ('Ejercicio N°2', layout)
    while True:
     event, values = window.read()
     if event in (sg.WIN_CLOSED, 'Cancel') :
        break
     window.close()