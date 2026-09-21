class Producto:

    def __init__(
            self,
            codigo,
            nombre,
            categoria,
            precio,
            stock
    ):

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.stock = int(stock)

    def convertir_a_diccionario(self):

        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def desde_diccionario(cls, datos):

        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["stock"]
        )

    def __str__(self):

        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: {self.precio} | "
            f"Stock: {self.stock}"
        )