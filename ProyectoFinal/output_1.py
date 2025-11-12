#!/usr/bin/env python3
# Compilado por Mini-Compilador GuionesLang (Fase 5)
# Proyecto Final - Compiladores
import sys
import time

current_item = 'Mano'
inventario = ['Mano']
item_properties = {
    # Incluye aquí la tabla de propiedades si fuera necesaria en tiempo de ejecución
}

def inicio_1():
    global current_item, inventario
    print("Test 1: Inicio y Mano.")
    print('\n--- Opciones ---')
    print(f' 1. Picar Árbol (Resistencia 1)')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "Picar Árbol (Resistencia 1)".lower().strip('"')]:
        print(f'\n>> [Saltando a picar_madera_obtiene_pico_1]...')
        picar_madera_obtiene_pico_1()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()

def picar_madera_obtiene_pico_1():
    global current_item, inventario
    print("Madera obtenida.")
    current_item = 'PicoMadera'
    if 'PicoMadera' not in inventario: inventario.append('PicoMadera')
    print(f'\n[ITEM]: ¡Obtenido PicoMadera! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    print(f' 1. Volver')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "Volver".lower().strip('"')]:
        print(f'\n>> [Saltando a inicio_1]...')
        inicio_1()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()

def fin_juego_1():
    global current_item, inventario
    print("Fin del juego 1.")


if __name__ == '__main__':
    try:
        print('--- JUEGO INICIADO ---')
        time.sleep(0.5)
        inicio_1()
    except Exception as e:
        print(f'\n[ERROR FATAL DE EJECUCIÓN]: {e}')
    except KeyboardInterrupt:
        print('\n[FIN DEL JUEGO]...')