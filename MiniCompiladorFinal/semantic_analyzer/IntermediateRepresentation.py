# Archivo: semantic_analyzer/IntermediateRepresentation.py
class IR:
    """
    Clase para almacenar la representación intermedia (TAC).
    """
    def __init__(self):
        self.instructions = []
        self.temp_counter = 0
        self.label_counter = 0

    def add_instruction(self, op, arg1=None, arg2=None, result=None):
        instruction = {
            'op': op,
            'arg1': arg1,
            'arg2': arg2,
            'result': result
        }
        self.instructions.append(instruction)

    def new_temp(self):
        self.temp_counter += 1
        return f"t{self.temp_counter}"

    def new_label(self):
        self.label_counter += 1
        return f"L{self.label_counter}"

    def __str__(self):
        output = []
        for inst in self.instructions:
            op = inst['op']
            if op.endswith(':'):
                output.append(f"{op}")
            elif op == '=':
                output.append(f"    {inst['result']} = {inst['arg1']}")
            elif op == 'if_false_goto':
                output.append(f"    if_false {inst['arg1']} goto {inst['result']}")
            elif op == 'CALL':
                output.append(f"    CALL {inst['result']}")
            elif op == 'PRINT':
                output.append(f"    PRINT {inst['arg1']}")
            elif op == 'RETURN':
                output.append(f"    RETURN")
            elif op == '':
                output.append("")
            else:
                output.append(f"    {inst}")
        return "\n".join(output)
