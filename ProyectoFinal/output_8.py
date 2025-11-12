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

def menu_8():
    global current_item, inventario
    print("Test 8: Referencia de Salida.")
    print('\n--- Opciones ---')
    print(f' 1. Salir del Juego')
    choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')
    if choice.strip().lower() in ['1', "Salir del Juego".lower().strip('"')]:
        print(f'\n>> [Saltando a fin_juego_8]...')
        fin_juego_8()
        return
    else:
        print('Opción inválida. Regresando a la escena.')
        globals()[sys._getframe(0).f_code.co_name]()

def fin_juego_8():
    global current_item, inventario
    print("El juego ha terminado.")


if __name__ == '__main__':
    try:
        print('--- JUEGO INICIADO ---')
        time.sleep(0.5)
        menu_8()
    except Exception as e:
        print(f'\n[ERROR FATAL DE EJECUCIÓN]: {e}')
    except KeyboardInterrupt:
        print('\n[FIN DEL JUEGO]...')