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

def inicio_10():
    global current_item, inventario
    print("Test 10: Ramificación Completa.")
    print('\n--- Opciones ---')
    print(f' 1. Picar')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "Picar".lower().strip('"')]:
        print(f'\n>> [Saltando a picar_madera_obtiene_pico_10]...')
        picar_madera_obtiene_pico_10()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()
    print('\n--- Opciones ---')
    print(f' 1. Terminar')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "Terminar".lower().strip('"')]:
        print(f'\n>> [Saltando a fin_juego_10]...')
        fin_juego_10()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()

def picar_madera_obtiene_pico_10():
    global current_item, inventario
    current_item = 'PicoMadera'
    if 'PicoMadera' not in inventario: inventario.append('PicoMadera')
    print(f'\n[ITEM]: ¡Obtenido PicoMadera! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    print(f' 1. OK')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "OK".lower().strip('"')]:
        print(f'\n>> [Saltando a fin_juego_10]...')
        fin_juego_10()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()

def fin_juego_10():
    global current_item, inventario
    print("Salida.")


if __name__ == '__main__':
    try:
        print('--- JUEGO INICIADO ---')
        time.sleep(0.5)
        inicio_10()
    except Exception as e:
        print(f'\n[ERROR FATAL DE EJECUCIÓN]: {e}')
    except KeyboardInterrupt:
        print('\n[FIN DEL JUEGO]...')