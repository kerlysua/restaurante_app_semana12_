class Usuario:

    def __init__(
            self,
            identificacion,
            nombre,
            contrasena
    ):

        self.identificacion = identificacion
        self.nombre = nombre
        self.contrasena = contrasena

    def convertir_a_diccionario(self):

        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "contrasena": self.contrasena
        }

    @classmethod
    def desde_diccionario(cls, datos):

        return cls(
            datos["identificacion"],
            datos["nombre"],
            datos["contrasena"]
        )

    def __str__(self):

        return (
            f"ID: {self.identificacion} | "
            f"Nombre: {self.nombre}"
        )