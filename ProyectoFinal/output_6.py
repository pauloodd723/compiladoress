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

def inicio_6():
    global current_item, inventario
    print("Test 6: PicoDiamante listo.")
    current_item = 'PicoDiamante'
    if 'PicoDiamante' not in inventario: inventario.append('PicoDiamante')
    print(f'\n[ITEM]: ¡Obtenido PicoDiamante! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    print(f' 1. Picar Netherite (Resistencia 6)')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "Picar Netherite (Resistencia 6)".lower().strip('"')]:
        print(f'\n>> [Saltando a picar_netherite_obtiene_pico_6]...')
        picar_netherite_obtiene_pico_6()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()

def picar_netherite_obtiene_pico_6():
    global current_item, inventario
    print("¡Victoria! Netherite obtenida.")
    print('\n--- Opciones ---')
    print(f' 1. Finalizar')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "Finalizar".lower().strip('"')]:
        print(f'\n>> [Saltando a juego_terminado_6]...')
        juego_terminado_6()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()

def juego_terminado_6():
    global current_item, inventario
    print("Juego completado.")


if __name__ == '__main__':
    try:
        print('--- JUEGO INICIADO ---')
        time.sleep(0.5)
        inicio_6()
    except Exception as e:
        print(f'\n[ERROR FATAL DE EJECUCIÓN]: {e}')
    except KeyboardInterrupt:
        print('\n[FIN DEL JUEGO]...')