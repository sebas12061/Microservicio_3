from repositories.mapas_repository import MapasRepository

class MapasService:
    def __init__(self):
        self.repo = MapasRepository()

    def listar_lugares(self):
        return self.repo.obtener_lugares()

    def filtrar_por_categoria(self, categoria):
        return self.repo.filtrar_lugares(categoria)
