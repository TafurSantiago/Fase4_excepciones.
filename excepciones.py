class SoftwareFJError(Exception):
    """Clase base para excepciones del sistema."""

    pass


class ReservaError(SoftwareFJError):
    """Error específico en el proceso de reserva."""

    pass


class ClienteInvalidoError(SoftwareFJError):
    """Error cuando los datos del cliente no cumplen las validaciones."""

    pass
