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

def inicio_4():
    global current_item, inventario
    print("Test 4: PicoCobre listo.")
    current_item = 'PicoCobre'
    if 'PicoCobre' not in inventario: inventario.append('PicoCobre')
    print(f'\n[ITEM]: ¡Obtenido PicoCobre! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    print(f' 1. Picar Hierro (Resistencia 4)')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "Picar Hierro (Resistencia 4)".lower().strip('"')]:
        print(f'\n>> [Saltando a picar_hierro_obtiene_pico_4]...')
        picar_hierro_obtiene_pico_4()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()

def picar_hierro_obtiene_pico_4():
    global current_item, inventario
    print("Hierro obtenido.")
    current_item = 'PicoHierro'
    if 'PicoHierro' not in inventario: inventario.append('PicoHierro')
    print(f'\n[ITEM]: ¡Obtenido PicoHierro! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    print(f' 1. Volver')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "Volver".lower().strip('"')]:
        print(f'\n>> [Saltando a inicio_4]...')
        inicio_4()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()


if __name__ == '__main__':
    try:
        print('--- JUEGO INICIADO ---')
        time.sleep(0.5)
        inicio_4()
    except Exception as e:
        print(f'\n[ERROR FATAL DE EJECUCIÓN]: {e}')
    except KeyboardInterrupt:
        print('\n[FIN DEL JUEGO]...')