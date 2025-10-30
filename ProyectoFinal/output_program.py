#!/usr/bin/env python3
# Compilado por Mini-Compilador GuionesLang (Fase 5)
import sys
import time

current_item = 'Mano'
inventario = ['Mano']

def inicio():
    global current_item, inventario
    print("Estás en el mundo. Tienes tu Mano (Fuerza 1).")
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Picar Árbol (Resistencia 1) (Escribe 1 o "Picar Árbol (Resistencia 1)")] -> ')
    if choice.strip().lower() in ['1', "Picar Árbol (Resistencia 1)".lower().strip('"')]:
        picar_madera_obtiene_pico()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Terminar (Escribe 1 o "Terminar")] -> ')
    if choice.strip().lower() in ['1', "Terminar".lower().strip('"')]:
        fin_juego()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()

def picar_madera_obtiene_pico():
    global current_item, inventario
    print("Madera obtenida. Ahora obtienes PicoMadera.")
    current_item = 'PicoMadera'
    if 'PicoMadera' not in inventario: inventario.append('PicoMadera')
    print(f'\n[ITEM]: ¡Obtenido PicoMadera! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Continuar a Nivel 2 (Escribe 1 o "Continuar a Nivel 2")] -> ')
    if choice.strip().lower() in ['1', "Continuar a Nivel 2".lower().strip('"')]:
        mineria_nivel_2()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Volver (Escribe 1 o "Volver")] -> ')
    if choice.strip().lower() in ['1', "Volver".lower().strip('"')]:
        inicio()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()

def mineria_nivel_2():
    global current_item, inventario
    print("Tienes tu PicoMadera (Fuerza 2). ¿Qué vas a picar?")
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Picar Piedra (Resistencia 2) (Escribe 1 o "Picar Piedra (Resistencia 2)")] -> ')
    if choice.strip().lower() in ['1', "Picar Piedra (Resistencia 2)".lower().strip('"')]:
        picar_piedra_obtiene_pico()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Volver (Escribe 1 o "Volver")] -> ')
    if choice.strip().lower() in ['1', "Volver".lower().strip('"')]:
        inicio()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()

def picar_piedra_obtiene_pico():
    global current_item, inventario
    print("Piedra obtenida. ¡Es hora de mejorar tu pico!")
    current_item = 'PicoPiedra'
    if 'PicoPiedra' not in inventario: inventario.append('PicoPiedra')
    print(f'\n[ITEM]: ¡Obtenido PicoPiedra! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Ir a Menú Nivel 3 (Escribe 1 o "Ir a Menú Nivel 3")] -> ')
    if choice.strip().lower() in ['1', "Ir a Menú Nivel 3".lower().strip('"')]:
        mineria_nivel_3()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Volver (Escribe 1 o "Volver")] -> ')
    if choice.strip().lower() in ['1', "Volver".lower().strip('"')]:
        inicio()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()

def mineria_nivel_3():
    global current_item, inventario
    print("Tienes tu PicoPiedra (Fuerza 3). ¿Qué vas a picar?")
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Picar Cobre (Resistencia 3) (Escribe 1 o "Picar Cobre (Resistencia 3)")] -> ')
    if choice.strip().lower() in ['1', "Picar Cobre (Resistencia 3)".lower().strip('"')]:
        picar_cobre_obtiene_pico()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Volver (Escribe 1 o "Volver")] -> ')
    if choice.strip().lower() in ['1', "Volver".lower().strip('"')]:
        inicio()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()

def picar_cobre_obtiene_pico():
    global current_item, inventario
    print("Cobre obtenido. ¡Tienes el PicoCobre!")
    current_item = 'PicoCobre'
    if 'PicoCobre' not in inventario: inventario.append('PicoCobre')
    print(f'\n[ITEM]: ¡Obtenido PicoCobre! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Picar Hierro (Resistencia 4) (Escribe 1 o "Picar Hierro (Resistencia 4)")] -> ')
    if choice.strip().lower() in ['1', "Picar Hierro (Resistencia 4)".lower().strip('"')]:
        picar_hierro_obtiene_pico()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Volver (Escribe 1 o "Volver")] -> ')
    if choice.strip().lower() in ['1', "Volver".lower().strip('"')]:
        inicio()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()

def picar_hierro_obtiene_pico():
    global current_item, inventario
    print("Hierro obtenido. ¡Tienes el PicoHierro!")
    current_item = 'PicoHierro'
    if 'PicoHierro' not in inventario: inventario.append('PicoHierro')
    print(f'\n[ITEM]: ¡Obtenido PicoHierro! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Picar Diamante (Resistencia 5) (Escribe 1 o "Picar Diamante (Resistencia 5)")] -> ')
    if choice.strip().lower() in ['1', "Picar Diamante (Resistencia 5)".lower().strip('"')]:
        picar_diamante_obtiene_pico()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Volver (Escribe 1 o "Volver")] -> ')
    if choice.strip().lower() in ['1', "Volver".lower().strip('"')]:
        inicio()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()

def picar_diamante_obtiene_pico():
    global current_item, inventario
    print("¡Diamante obtenido!")
    current_item = 'PicoDiamante'
    if 'PicoDiamante' not in inventario: inventario.append('PicoDiamante')
    print(f'\n[ITEM]: ¡Obtenido PicoDiamante! Estado actual: {current_item}')
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Picar Netherite (Resistencia 6) (Escribe 1 o "Picar Netherite (Resistencia 6)")] -> ')
    if choice.strip().lower() in ['1', "Picar Netherite (Resistencia 6)".lower().strip('"')]:
        picar_netherite()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Volver (Escribe 1 o "Volver")] -> ')
    if choice.strip().lower() in ['1', "Volver".lower().strip('"')]:
        inicio()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()

def picar_netherite():
    global current_item, inventario
    print("¡Felicidades! Has obtenido el material más fuerte del juego: Netherite.")
    print('\n--- Opciones ---')
    choice = input(f'[Opción: Finalizar Juego (Escribe 1 o "Finalizar Juego")] -> ')
    if choice.strip().lower() in ['1', "Finalizar Juego".lower().strip('"')]:
        juego_terminado()
    else:
        print('Opción inválida. Reintentando...')
        globals()[sys._getframe(0).f_code.co_name]()

def juego_terminado():
    global current_item, inventario
    print("¡TE PASASTE EL JUEGO! La Netherite es tuya.")

def fin_juego():
    global current_item, inventario
    print("El juego ha terminado.")


if __name__ == '__main__':
    try:
        inicio()
    except RecursionError:
        print('\n[ERROR]: El juego ha entrado en un bucle infinito.')
    except KeyboardInterrupt:
        print('\n[FIN DEL JUEGO]...')