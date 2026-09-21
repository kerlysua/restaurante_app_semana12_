import json
import os


class ArchivoServicio:

    def __init__(self):

        base = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        self.ruta_productos = os.path.join(
            base,
            "datos",
            "productos.json"
        )

        self.ruta_usuarios = os.path.join(
            base,
            "datos",
            "usuarios.json"
        )

        self.ruta_ventas = os.path.join(
            base,
            "datos",
            "ventas.json"
        )

    def guardar_productos(self, productos):

        datos = [
            p.convertir_a_diccionario()
            for p in productos
        ]

        self._guardar_json(
            self.ruta_productos,
            datos
        )

    def guardar_usuarios(self, usuarios):

        datos = [
            u.convertir_a_diccionario()
            for u in usuarios
        ]

        self._guardar_json(
            self.ruta_usuarios,
            datos
        )

    def guardar_ventas(self, ventas):

        datos = [
            v.convertir_a_diccionario()
            for v in ventas
        ]

        self._guardar_json(
            self.ruta_ventas,
            datos
        )

    def cargar_productos(self):

        return self._cargar_json(
            self.ruta_productos
        )

    def cargar_usuarios(self):

        return self._cargar_json(
            self.ruta_usuarios
        )

    def cargar_ventas(self):

        return self._cargar_json(
            self.ruta_ventas
        )

    def _guardar_json(
            self,
            ruta,
            datos
    ):

        with open(
                ruta,
                "w",
                encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def _cargar_json(
            self,
            ruta
    ):

        try:

            with open(
                    ruta,
                    "r",
                    encoding="utf-8"
            ) as archivo:

                return json.load(archivo)

        except FileNotFoundError:
            return []