class SoftwareFJError(Exception):
    """Excepción base para todos los errores del sistema Software FJ."""
    pass

class ClienteInvalidoError(SoftwareFJError):
    pass

class ServicioInvalidoError(SoftwareFJError):
    pass

class ReservaInvalidaError(SoftwareFJError):
    pass

class OperacionNoPermitidaError(SoftwareFJError):
    pass
