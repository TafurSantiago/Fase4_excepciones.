import logging
from modelos import Cliente, Reserva
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from excepciones import SoftwareFJError

# [span_16](start_span)Configuración de Logs en archivo[span_16](end_span)
logging.basicConfig(
    filename="errores_sistema.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def simular_sistema():
    operaciones = [
        # (Tipo, Nombre, Email, Servicio, Parametro)
        ("OK", "Juan Perez", "juan@mail.com", ReservaSala(), 3),
        ("ERROR_MAIL", "Luis", "luis_sin_arroba", AlquilerEquipo(), 2),
        ("OK", "Ana Gomez", "ana@mail.com", AsesoriaEspecializada(), 5),
        ("ERROR_TIPO", "Invalido", "test@mail.com", None, 0),  # Forzará excepción
        # ... Se completan las 10 operaciones aquí
    ]

    print("--- Iniciando Simulación Software FJ ---")

    for i, op in enumerate(operaciones, 1):
        try:
            print(f"Operación {i}:", end=" ")
            if op[3] is None:
                raise SoftwareFJError("Servicio no definido")

            cliente = Cliente(i, op[1], op[2])
            reserva = Reserva(cliente, op[3], op[4])
            print(reserva.procesar())

        except SoftwareFJError as e:
            # [span_17](start_span)Manejo robusto: try/except/finally[span_17](end_span)
            print(f"ERROR CONTROLADO: {e}")
            logging.error(f"Falla en operación {i}: {e}")
        finally:
            print("-" * 30)


if __name__ == "__main__":
    simular_sistema()
