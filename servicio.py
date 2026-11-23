from abc import abstractmethod
from entidad import Entidad
from excepciones import ServicioInvalidoError

class Servicio(Entidad):
    def __init__(self, identificador, nombre_servicio, tarifa_base):
        super().__init__(identificador)
        self.nombre_servicio = nombre_servicio
        self.tarifa_base = tarifa_base

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @tarifa_base.setter
    def tarifa_base(self, valor):
        if valor <= 0:
            raise ServicioInvalidoError(f"La tarifa base debe ser mayor a cero. Valor: {valor}")
        self._tarifa_base = float(valor)

    @abstractmethod
    def validar_parametros(self, *args, **kwargs):
        pass

    @abstractmethod
    def calcular_costo(self, duracion, **kwargs):
        pass

    def obtener_informacion(self):
        return f"Servicio: {self.nombre_servicio} - Tarifa: ${self.tarifa_base}"


class ReservaSala(Servicio):
    def __init__(self, identificador, tarifa_base, capacidad, incluye_proyector):
        super().__init__(identificador, "Reserva de Sala", tarifa_base)
        self.capacidad = capacidad
        self.incluye_proyector = incluye_proyector

    def validar_parametros(self, duracion, asistentes=1, **kwargs):
        if duracion <= 0:
            raise ServicioInvalidoError("La duración debe ser mayor a 0 horas.")
        if asistentes > self.capacidad:
            raise ServicioInvalidoError(f"Asistentes ({asistentes}) exceden la capacidad ({self.capacidad}).")
        return True

    def calcular_costo(self, duracion, descuento=0.0, impuesto=0.19, **kwargs):
        self.validar_parametros(duracion, kwargs.get('asistentes', 1))
        costo = self.tarifa_base * duracion
        if self.incluye_proyector:
            costo += 20.0
        return round(costo * (1.0 - descuento) * (1.0 + impuesto), 2)


class AlquilerEquipo(Servicio):
    def __init__(self, identificador, tarifa_base, tipo_equipo, garantia_requerida):
        super().__init__(identificador, "Alquiler de Equipo", tarifa_base)
        self.tipo_equipo = tipo_equipo
        self.garantia_requerida = garantia_requerida

    def validar_parametros(self, duracion, unidades=1, **kwargs):
        if duracion <= 0 or unidades <= 0:
            raise ServicioInvalidoError("Duración y unidades deben ser mayores a 0.")
        return True

    def calcular_costo(self, duracion, unidades=1, descuento=0.0, impuesto=0.19, **kwargs):
        self.validar_parametros(duracion, unidades)
        costo = self.tarifa_base * duracion * unidades
        if self.garantia_requerida:
            costo += 50.0
        return round(costo * (1.0 - descuento) * (1.0 + impuesto), 2)


class AsesoriaEspecializada(Servicio):
    def __init__(self, identificador, tarifa_base, area_experticia, nivel_senior):
        super().__init__(identificador, "Asesoría Especializada", tarifa_base)
        self.area_experticia = area_experticia
        self.nivel_senior = nivel_senior

    def validar_parametros(self, duracion, **kwargs):
        if duracion <= 0:
            raise ServicioInvalidoError("La duración debe ser mayor a 0 horas.")
        return True

    def calcular_costo(self, duracion, descuento=0.0, impuesto=0.19, horas_urgentes=0.0, **kwargs):
        self.validar_parametros(duracion)
        mult = 1.5 if self.nivel_senior else 1.0
        costo = (self.tarifa_base * mult * duracion) + (horas_urgentes * 30.0)
        return round(costo * (1.0 - descuento) * (1.0 + impuesto), 2)
