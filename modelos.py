from abc import ABC, abstractmethod
from excepciones import ClienteInvalidoError


class EntidadBase(ABC):
    """Clase abstracta para entidades generales[span_11](end_span)"""

    @abstractmethod
    def obtener_detalles(self):
        pass


class Cliente(EntidadBase):
    def _init_(self, id_cliente, nombre, email):
        self.__id = id_cliente  # Encapsulación[span_12](end_span)
        self.nombre = nombre
        self.__validar_email(email)
        self.email = email

    def __validar_email(self, email):
        if "@" not in email:
            raise ClienteInvalidoError(f"Email inválido: {email}")

    def obtener_detalles(self):
        return f"Cliente: {self.nombre} (ID: {self.__id})"


class Reserva:
    def _init_(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def procesar(self):
        # [span_13](start_span)Polimorfismo al llamar a calcular_costo()[span_13](end_span)
        costo = self.servicio.calcular_costo(self.duracion)
        self.estado = "Confirmada"
        return f"Reserva {self.estado} para {self.cliente.nombre}. Costo: ${costo}"
