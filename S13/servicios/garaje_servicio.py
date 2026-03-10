from modelos.vehiculo import Vehiculo

class GarajeServicio:
    """
    Clase que contiene la lógica de negocio para la gestión del garaje.
    """
    def __init__(self):
        # Lista para almacenar los vehículos registrados en memoria
        self._vehiculos = []

    def agregar_vehiculo(self, placa, marca, propietario):
        """
        Crea un nuevo objeto Vehiculo y lo agrega a la lista.
        """
        if not placa or not marca or not propietario:
            raise ValueError("Todos los campos son obligatorios.")
        
        nuevo_vehiculo = Vehiculo(placa, marca, propietario)
        self._vehiculos.append(nuevo_vehiculo)
        return nuevo_vehiculo

    def obtener_vehiculos(self):
        """
        Retorna la lista de vehículos registrados.
        """
        return self._vehiculos

    def limpiar_registros(self):
        """
        Limpia todos los registros del garaje.
        """
        self._vehiculos.clear()
