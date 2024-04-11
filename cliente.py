class Cliente:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def toDBCollection(self):
        return{
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad
        }