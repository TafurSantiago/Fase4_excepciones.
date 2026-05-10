from abc import ABC, abstractmethod


class Servicio(ABC):
    @abstractmethod
    def calcular_costo(self, parametro):
        pass

    @abstractmethod
    def describir(self):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, horas, tarifa_base=50):
        # [span_14](start_span)Ejemplo de sobrecarga lógica (parámetros opcionales)[span_14](end_span)
        return horas * tarifa_base

    def describir(self):
        return "Servicio de Reserva de Salas de Juntas."


class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        return dias * 30

    def describir(self):
        return "Alquiler de equipos de cómputo."


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas):
        return horas * 100

    def describir(self):
        return "Asesoría técnica especializada."
