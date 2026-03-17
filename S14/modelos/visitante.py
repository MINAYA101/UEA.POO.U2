class Visitante:
    def __init__(self, cedula, nombre, motivo):
        self.cedula = cedula
        self.nombre = nombre
        self.motivo = motivo

    def __str__(self):
        return f"Visitante [Cédula: {self.cedula}, Nombre: {self.nombre}, Motivo: {self.motivo}]"
