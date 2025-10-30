# Archivo: semantic_analyzer/SymbolTable.py

class SemanticError(Exception):
    pass

class SymbolTable:
    def __init__(self):
        self.scenes = {} 
        self.item_properties = {} # { 'PicoMadera': {'fuerza': 2}, 'Piedra': {'resistencia': 2} }
        
        # Estado Inicial del Jugador (Para la validación del Visitor)
        self.global_state = {'current_item': 'Mano', 'inventario': ['Mano']}

    def add_scene(self, name, line):
        if name in self.scenes:
            raise SemanticError(f"Error Semántico: La escena '{name}' ya ha sido declarada en línea {self.scenes[name]['line']} y se intenta redeclarar en línea {line}.")
        self.scenes[name] = {'type': 'Scene', 'line': line}

    def exists_scene(self, name):
        return name in self.scenes

    # --- Métodos para Carga Externa (FASE 0) ---
    def add_item_property(self, item_id, prop_name, value):
        """Almacena la fuerza/resistencia del ítem cargado desde el CSV."""
        prop_name = prop_name.lower() 
        if item_id not in self.item_properties:
            self.item_properties[item_id] = {}
        
        try:
            self.item_properties[item_id][prop_name] = int(value)
        except ValueError:
            print(f"Advertencia: Valor de propiedad no numérico para {item_id}.")
            self.item_properties[item_id][prop_name] = 0

    # --- Métodos para Validación (FASE 3) ---
    def get_item_force(self, item_id):
        """Retorna la fuerza del ítem."""
        return self.item_properties.get(item_id, {}).get('fuerza', 0)

    def get_material_resistance(self, target_scene_id):
        """Determina la resistencia requerida por la escena de minería."""
        # Se asume que la escena de minería es siempre 'picar_MATERIAL'
        parts = target_scene_id.split('_')
        if len(parts) < 2 or parts[0] != 'picar':
            return 0 
            
        # El material es la segunda palabra: picar_Piedra -> 'Piedra'
        material_id = parts[1].capitalize() 
        return self.item_properties.get(material_id, {}).get('resistencia', 9999)