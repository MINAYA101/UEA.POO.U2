class Vehiculo:
    """
    Clase que representa un vehículo en el sistema de gestión de garaje.
    """
    def __init__(self, placa, marca, propietario):
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    def __str__(self):
        return f"Vehículo [Placa: {self.placa}, Marca: {self.marca}, Propietario: {self.propietario}]"
