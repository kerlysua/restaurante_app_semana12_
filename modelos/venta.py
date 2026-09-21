class Venta:

    def __init__(
            self,
            usuario_id,
            producto_codigo,
            cantidad
    ):

        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = int(cantidad)

    def convertir_a_diccionario(self):

        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos):

        return cls(
            datos["usuario_id"],
            datos["producto_codigo"],
            datos["cantidad"]
        )

    def __str__(self):

        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )