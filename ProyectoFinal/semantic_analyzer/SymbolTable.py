# Archivo: semantic_analyzer/SymbolTable.py

class SemanticError(Exception):
    pass

class SymbolTable:
    def __init__(self):
        self.scenes = {} 
        self.errors = []
        
        # --- DATOS INTEGRADOS (REEMPLAZO DEL CSV para Fase 3) ---
        self.item_properties = {
            'Mano': {'fuerza': 1, 'resistencia': 1},
            'PicoMadera': {'fuerza': 2, 'resistencia': 2},
            'PicoPiedra': {'fuerza': 3, 'resistencia': 3},
            'PicoCobre': {'fuerza': 4, 'resistencia': 4},
            'PicoHierro': {'fuerza': 5, 'resistencia': 5},
            'PicoDiamante': {'fuerza': 6, 'resistencia': 6},
            'PicoNetherite': {'fuerza': 7, 'resistencia': 7},
            
            # Resistencia de los Materiales
            'Madera': {'resistencia': 1},
            'Piedra': {'resistencia': 2},
            'Cobre': {'resistencia': 3},
            'Hierro': {'resistencia': 4},
            'Diamante': {'resistencia': 5},
            'Netherite': {'resistencia': 6}
        }
        # --------------------------------------------------------
        
        self.global_state = {'current_item': 'Mano', 'inventario': ['Mano']}

    def add_scene(self, name, line):
        if name in self.scenes:
            raise SemanticError(f"Error Semántico: La escena '{name}' ya ha sido declarada en línea {self.scenes[name]['line']} y se intenta redeclarar en línea {line}.")
        self.scenes[name] = {'type': 'Scene', 'line': line}

    def exists_scene(self, name):
        return name in self.scenes

    def get_item_force(self, item_id):
        """Retorna la fuerza del ítem."""
        return self.item_properties.get(item_id, {}).get('fuerza', 0)

    def get_material_resistance(self, target_scene_id):
        """Determina la resistencia requerida por la escena de minería."""
        parts = target_scene_id.split('_')
        if len(parts) < 2 or parts[0] != 'picar':
            return 0 
            
        material_id = parts[1].capitalize() 
        return self.item_properties.get(material_id, {}).get('resistencia', 9999)