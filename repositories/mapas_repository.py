from models.lugar import Lugar

class MapasRepository:
    def __init__(self):
        # Lista simulada de lugares que ya están aprobados
        self.lugares = [
            Lugar(1, "Parque Central", "naturaleza", "Calle 10 #5-20", "aceptado"),
            Lugar(2, "Museo de Arte", "cultura", "Carrera 8 #15-33", "aceptado")
        ]

    def obtener_lugares(self):
        return [lugar.to_dict() for lugar in self.lugares]

    def filtrar_lugares(self, categoria=None):
        if categoria:
            return [lugar.to_dict() for lugar in self.lugares if lugar.categoria == categoria]
        return [lugar.to_dict() for lugar in self.lugares]
