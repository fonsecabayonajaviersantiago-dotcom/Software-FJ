# Sistema Integral Software FJ

Descripcion
Sistema de gestion orientado a objetos desarrollado en Python para la empresa Software FJ, disenado sin bases de datos y enfocado en la robustez, modularidad y el manejo avanzado de excepciones.

Estructura del Proyecto
El sistema esta modularizado en varios archivos aplicando estrictos principios de Programacion Orientada a Objetos (OOP):

* main.py: Script principal que ejecuta la simulacion de las 10 operaciones completas (validas e invalidas).
* entidad.py: Clase abstracta base que define la estructura general de las entidades del sistema.
* cliente.py: Clase que gestiona los datos personales de los clientes con validaciones estrictas y encapsulacion.
* servicio.py: Clase abstracta de servicios y sus implementaciones polimorficas especializadas (ReservaSala, AlquilerEquipo, AsesoriaEspecializada).
* reserva.py: Integra cliente, servicio, duracion y estados, gestionando el ciclo de vida de la reserva.
* excepciones.py: Jerarquia de excepciones personalizadas y manejo de errores.
* logs.py: Configuracion para el registro automatico de eventos y errores.
* software_fj.log: Archivo de salida donde se registran todos los logs del sistema.

Principios de OOP Aplicados

* Abstraccion: Clases base abstractas con metodos obligatorios.
* Herencia: Jerarquia de servicios y excepciones personalizadas.
* Polimorfismo: Sobrescritura de metodos para el calculo de costos adaptados a cada servicio.
* Encapsulacion: Uso de propiedades y validaciones de entrada estrictas.

Como Ejecutar

1. Extraiga la carpeta del proyecto.
2. Abra Visual Studio Code.
3. Seleccione Archivo y Abrir carpeta, luego elija la carpeta del proyecto.
4. Abra el archivo main.py.
5. Abra la terminal integrada en Visual Studio Code.
6. Ejecute el siguiente comando:
python main.py
(Si este comando no funciona en Windows, pruebe con py main.py)
7. Revise la salida de la terminal y el archivo generado software_fj.log.


