"""
Contiene la clase InfoActa e
internamente tiene sus respectivos atributos.
Asignatura: POO
"""


class InfoActa:

    # Constructor
    def __init__(self, criterios) -> None:
        super().__init__()

        # Datos del acta
        self.autor = ""
        self.fecha_acta = ""
        self.fecha_presentacion = ""
        self.nombre_trabajo = ""
        self.tipo_trabajo = ""
        self.director = ""
        self.codirector = " "
        self.tipo_jurado1 = ""
        self.tipo_jurado2 = ""
        self.jurado1 = ""
        self.jurado2 = ""
        self.nota_final = 0.0
        self.criterios = criterios
        self.info_adicional = ""
        self.restriccion_nota_final = 0.0
        self.estado = False
