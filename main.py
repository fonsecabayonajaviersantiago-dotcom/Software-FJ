from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ClienteInvalidoError, ServicioInvalidoError, ReservaInvalidaError, OperacionNoPermitidaError
from logs import LOG_FILE

def ejecutar_simulacion():
    print("=== INICIANDO SIMULACIÓN DE 10 OPERACIONES ===")
    clientes, servicios, reservas = [], [], []

    # Op 1
    try:
        c1 = Cliente("CLI-001", "Carlos Pérez", "carlos@softwarefj.com", "3101234567")
        clientes.append(c1)
        print("1. Cliente registrado con éxito.")
    except Exception as e: print(e)

    # Op 2
    try:
        Cliente("CLI-002", "Ana", "correo-malo", "abc")
    except ClienteInvalidoError:
        print("2. Excepción controlada: Cliente inválido detectado.")

    # Op 3
    try:
        s1 = ReservaSala("SRV-101", 50.0, 10, True)
        servicios.append(s1)
        print("3. Servicio de sala creado con éxito.")
    except Exception as e: print(e)

    # Op 4
    try:
        ReservaSala("SRV-102", -10.0, 5, False)
    except ServicioInvalidoError:
        print("4. Excepción controlada: Tarifa negativa detectada.")

    # Op 5
    try:
        s2 = AlquilerEquipo("SRV-201", 30.0, "Laptop", True)
        s3 = AsesoriaEspecializada("SRV-301", 80.0, "Cloud", True)
        servicios.extend([s2, s3])
        print("5. Servicios adicionales creados con éxito.")
    except Exception as e: print(e)

    # Op 6
    try:
        c2_valido = Cliente("CLI-003", "María Rodríguez", "maria@gmail.com", "3209876543")
        clientes.append(c2_valido)
        print("6. Segundo cliente registrado correctamente.")
    except Exception as e: print(e)

    # Op 7
    try:
        r1 = Reserva("RES-001", clientes[0], servicios[0], 3.0, asistentes=4, descuento=0.1)
        r1.procesar_reserva()
        reservas.append(r1)
        print("7. Reserva de sala procesada con éxito.")
    except Exception as e: print(e)

    # Op 8
    try:
        r2 = Reserva("RES-002", clientes[1], servicios[1], 5.0, unidades=2)
        r2.procesar_reserva()
        reservas.append(r2)
        print("8. Alquiler de equipo procesado con éxito.")
    except Exception as e: print(e)

    # Op 9
    try:
        r3 = Reserva("RES-003", clientes[0], servicios[0], 2.0, asistentes=20)
        r3.procesar_reserva()
    except ReservaInvalidaError:
        print("9. Excepción controlada: Reserva fallida por exceso de capacidad.")

    # Op 10
    try:
        reservas[0].cancelar_reserva()
        print("10. Reserva cancelada exitosamente.")
        reservas[0].cancelar_reserva()
    except OperacionNoPermitidaError:
        print("10. Excepción controlada: Operación no permitida detectada.")

    print(f"\nSimulación finalizada. Revisa el archivo '{LOG_FILE}' para ver los logs.")

if __name__ == "__main__":
    ejecutar_simulacion()
