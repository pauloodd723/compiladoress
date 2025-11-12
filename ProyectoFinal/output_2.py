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

def inicio_2():
    global current_item, inventario
    print("Test 2: PicoMadera listo.")
    current_item = 'PicoMadera'
    if 'PicoMadera' not in inventario: inventario.append('PicoMadera')
    print(f'\n[ITEM]: ¡Obtenido PicoMadera! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    print(f' 1. Picar Piedra (Resistencia 2)')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "Picar Piedra (Resistencia 2)".lower().strip('"')]:
        print(f'\n>> [Saltando a picar_piedra_obtiene_pico_2]...')
        picar_piedra_obtiene_pico_2()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()

def picar_piedra_obtiene_pico_2():
    global current_item, inventario
    print("Piedra obtenida.")
    current_item = 'PicoPiedra'
    if 'PicoPiedra' not in inventario: inventario.append('PicoPiedra')
    print(f'\n[ITEM]: ¡Obtenido PicoPiedra! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    print(f' 1. Volver')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "Volver".lower().strip('"')]:
        print(f'\n>> [Saltando a inicio_2]...')
        inicio_2()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()


if __name__ == '__main__':
    try:
        print('--- JUEGO INICIADO ---')
        time.sleep(0.5)
        inicio_2()
    except Exception as e:
        print(f'\n[ERROR FATAL DE EJECUCIÓN]: {e}')
    except KeyboardInterrupt:
        print('\n[FIN DEL JUEGO]...')