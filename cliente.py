class Cliente:
    def __init__(self, nombre, apellido, edad):
        # Método de inicialización de la clase Cliente
        self.nombre = nombre  # Establece el atributo 'nombre' del cliente
        self.apellido = apellido  # Establece el atributo 'apellido' del cliente
        self.edad = edad  # Establece el atributo 'edad' del cliente

    def toDBCollection(self):
        # Método para convertir el objeto Cliente en un diccionario para almacenar en una base de datos
        return {
            'nombre': self.nombre,  # Añade el nombre del cliente al diccionario
            'apellido': self.apellido,  # Añade el apellido del cliente al diccionario
            'edad': self.edad  # Añade la edad del cliente al diccionario
        }
