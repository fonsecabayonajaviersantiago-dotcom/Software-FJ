# Sistema Integral Software FJ 🚀

Sistema de gestión orientado a objetos desarrollado en **Python** para la empresa *Software FJ*, diseñado sin bases de datos y enfocado en la robustez, modularidad y el manejo avanzado de excepciones.

## 🏛️ Estructura del Proyecto

El sistema está modularizado en varios archivos aplicando estrictos principios de Programación Orientada a Objetos (OOP):

- **`main.py`**: Script principal que ejecuta la simulación de las 10 operaciones completas (válidas e inválidas).
- **`entidad.py`**: Clase abstracta base (`Entidad`) que define la estructura general de las entidades del sistema.
- **`cliente.py`**: Clase que gestiona los datos personales de los clientes con validaciones estrictas y encapsulación (`@property`).
- **`servicio.py`**: Clase abstracta de servicios y sus implementaciones polimórficas especializadas:
  - `ReservaSala`
  - `AlquilerEquipo`
  - `AsesoriaEspecializada`
- **`reserva.py`**: Integra cliente, servicio, duración y estados, gestionando el ciclo de vida de la reserva.
- **`excepciones.py`**: Jerarquía de excepciones personalizadas y manejo de errores.
- **`logs.py`**: Configuración para el registro automático de eventos y errores.
- **`software_fj.log`**: Archivo de salida donde se registran todos los logs del sistema.

## ⚙️ Cómo Ejecutar

1. Extraiga la carpeta del proyecto.
2. Abra **Visual Studio Code**.
3. Seleccione **Archivo > Abrir carpeta** y elija la carpeta del proyecto.
4. Abra el archivo `main.py`.
5. Abra la terminal integrada en Visual Studio Code.
6. Ejecute el siguiente comando:
   ```bash
   python main.py
