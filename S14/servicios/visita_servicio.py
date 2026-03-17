from modelos.visitante import Visitante

class VisitaServicio:
    def __init__(self):
        # Lista privada para almacenar los visitantes en memoria
        self.__visitantes = []

    def registrar_visitante(self, cedula, nombre, motivo):
        if not cedula or not nombre or not motivo:
            raise ValueError("Todos los campos son obligatorios.")
        
        # Verificar si la cédula ya existe para evitar duplicados
        for v in self.__visitantes:
            if v.cedula == cedula:
                raise ValueError(f"Ya existe un visitante registrado con la cédula {cedula}.")
        
        nuevo_visitante = Visitante(cedula, nombre, motivo)
        self.__visitantes.append(nuevo_visitante)
        return nuevo_visitante

    def obtener_visitantes(self):
        return self.__visitantes

    def eliminar_visitante(self, cedula):
        visitante_a_eliminar = None
        for v in self.__visitantes:
            if v.cedula == cedula:
                visitante_a_eliminar = v
                break
        
        if visitante_a_eliminar:
            self.__visitantes.remove(visitante_a_eliminar)
            return True
        return False
