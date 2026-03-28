from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = []
        self.next_id = 1

    def agregar_tarea(self, descripcion):
        tarea = Tarea(self.next_id, descripcion)
        self.tareas.append(tarea)
        self.next_id += 1
        return tarea

    def completar_tarea(self, tarea_id):
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                tarea.estado_completado = True
                return True
        return False

    def eliminar_tarea(self, tarea_id):
        self.tareas = [tarea for tarea in self.tareas if tarea.id != tarea_id]
        return True

    def listar_tareas(self):
        return self.tareas
