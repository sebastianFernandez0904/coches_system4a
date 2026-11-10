from conexionBD import conexion, cursor


class CochesBD:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def insertar(self):
        try:
            cursor.execute(
                "insert into coches values(NULL, %s, %s, %s, %s, %s, %s)",
                (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def consultar(self):
        try:
            cursor.execute("select * from coches")
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def eliminar(self, id):
        try:
            cursor.execute("delete from coches where id = %s", (id,))
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def actualizar(self, id):
        try:
            cursor.execute(
                "update coches set marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s, asientos=%s where id=%s",
                (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    # Getters + Setters
    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

    def getModelo(self):
        return self._modelo

    def setModelo(self, modelo):
        self._modelo = modelo

    def getVelocidad(self):
        return self._velocidad

    def setVelocidad(self, velocidad):
        self._velocidad = velocidad

    def getPotencia(self):
        return self._potencia

    def setPotencia(self, potencia):
        self._potencia = potencia

    def getAsientos(self):
        return self._asientos

    def setAsientos(self, asientos):
        self._asientos = asientos

        