from cliente import Cliente
from servicio import Servicio
from excepciones import ReservaInvalidaError, OperacionNoPermitidaError
from logs import logger

class Reserva:
    ESTADOS_VALIDOS = {"Pendiente", "Confirmada", "Cancelada", "Procesada", "Fallida"}

    def __init__(self, id_reserva, cliente: Cliente, servicio: Servicio, duracion, **kwargs):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.kwargs = kwargs
        self.estado = "Pendiente"
        self.costo_total = 0.0

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo):
        if nuevo not in self.ESTADOS_VALIDOS:
            raise ReservaInvalidaError(f"Estado no válido: {nuevo}")
        self._estado = nuevo

    def procesar_reserva(self):
        try:
            if not self.cliente.validar() or not self.servicio.validar_parametros(self.duracion, **self.kwargs):
                raise OperacionNoPermitidaError("Entidades o parámetros inválidos.")
            self.costo_total = self.servicio.calcular_costo(self.duracion, **self.kwargs)
        except Exception as e:
            self.estado = "Fallida"
            logger.error(f"Error en reserva {self.id_reserva}: {e}")
            raise ReservaInvalidaError(f"Falla al procesar reserva {self.id_reserva}") from e
        else:
            self.estado = "Confirmada"
            logger.info(f"Reserva {self.id_reserva} confirmada. Total: ${self.costo_total}")
        finally:
            logger.info(f"Cierre de proceso para reserva {self.id_reserva}.")

    def cancelar_reserva(self):
        if self.estado in {"Confirmada", "Pendiente"}:
            self.estado = "Cancelada"
            logger.info(f"Reserva {self.id_reserva} cancelada.")
        else:
            raise OperacionNoPermitidaError(f"No se puede cancelar en estado {self.estado}.")

    def obtener_detalle(self):
        return f"Reserva [{self.id_reserva}] - Estado: {self.estado} - Costo: ${self.costo_total}"
