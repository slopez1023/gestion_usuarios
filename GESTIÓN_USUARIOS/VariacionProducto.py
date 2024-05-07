class VariacionProducto:
    def _init_(self, id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, material_variacion, color_variacion, id_producto_padre):
        self.id_variacion_producto = id_variacion_producto
        self.sku_variacion = sku_variacion
        self.descripcion_variacion = descripcion_variacion
        self.precio_variacion = precio_variacion
        self.material_variacion = material_variacion
        self.color_variacion = color_variacion
        self.id_producto_padre = id_producto_padre

    # ... (métodos específicos de la variación)

class VariacionSimpleFactory:
    @staticmethod
    def crear_variacion(tipo_variacion, **kwargs):
        if tipo_variacion == "Color":
            return VariacionColor(**kwargs)
        elif tipo_variacion == "Material":
            return VariacionMaterial(**kwargs)
        elif tipo_variacion == "Tamaño":
            return VariacionTamano(**kwargs)
        else:
            raise ValueError(f"Tipo de variación no válido: {tipo_variacion}")

class VariacionColor(VariacionProducto):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.color_variacion = kwargs["color"]

class VariacionMaterial(VariacionProducto):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.material_variacion = kwargs["material"]

class VariacionTamano(VariacionProducto):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.tamano_variacion = kwargs["tamano"]
