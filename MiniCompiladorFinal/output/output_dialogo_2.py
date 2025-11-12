# --- Código Python Generado Automáticamente ---

# --- Definición de Escenas (Funciones) ---

def inicio():
    print("Despiertas en una villa.")
    op_2 = input("Hablar con aldeano -> ")
    if op_2 == "Hablar con aldeano":
        plaza()
    return

def plaza():
    print("El aldeano te ofrece una misión.")
    op_7 = input("Aceptar misión -> ")
    if op_7 == "Aceptar misión":
        bosque()
    op_9 = input("Rechazar -> ")
    if op_9 == "Rechazar":
        casa()
    return

def casa():
    print("Te quedas en casa descansando.")
    return

# --- Punto de Entrada ---
if __name__ == '__main__':
    print('--- Iniciando Juego ---')
    inicio()
    print('--- Fin del Juego ---')