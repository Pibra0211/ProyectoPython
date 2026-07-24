# DriveSafe

Sistema de consola desarrollado en Python para la gestión de una academia de conducción. Permite registrar clientes, instructores y vehículos, programar citas de práctica, registrar la asistencia y las observaciones de cada práctica, y consultar el historial de un cliente.

## Autores

- Brajhan David Rivera Duarte
- Gerónimo Gómez Acevedo


## Estructura del proyecto

ProyectoPython/
├── base.py # Punto de entrada: menú principal del programa
├── clientes.py # Registro y consulta de clientes
├── instructores.py # Registro y consulta de instructores
├── vehiculos.py # Registro y consulta de vehículos
├── programarCitas.py # Programación de citas, asistencia e historial
└── data/
├── clientes.json
├── instructores.json
├── vehiculos.json
└── citas.json


Cada módulo de entidad (`clientes.py`, `instructores.py`, `vehiculos.py`) es responsable de su propio registro, validación y persistencia. `programarCitas.py` importa los tres módulos anteriores para poder validar disponibilidad y compatibilidad entre cliente, instructor y vehículo al momento de programar una cita.

## Cómo ejecutarlo

Desde la carpeta del proyecto:

python base.py


Esto abre el menú principal, desde el cual se accede a cada funcionalidad. También es posible ejecutar cada módulo por separado (por ejemplo `python clientes.py`) para probar únicamente su ciclo de registro.

## Menú principal

---Bienvenido a DriveSafe---

Registrar cliente
Registrar instructor
Registrar vehículo
Programar cita
Consultar citas programadas
Registrar asistencia y observaciones
Consultar historial de prácticas
Salir

## Estructura de datos

Cada módulo mantiene un diccionario en memoria indexado por una clave única:

| Módulo             | Diccionario   | Clave         |
|---------------------|---------------|---------------|
| `clientes.py`       | `clientes`    | número de documento |
| `instructores.py`   | `instructores`| número de documento |
| `vehiculos.py`      | `vehiculos`   | placa |
| `programarCitas.py` | `citas`       | id de cita (`CITA001`, `CITA002`, ...) |

Cada entrada del diccionario contiene, a su vez, un diccionario con los datos del registro. Por ejemplo, en `clientes`:

```python
clientes["12345678"] = {
    "nombre": "Juan Pérez",
    "edad": 25,
    "telefono": "+57 3001234567",
    "tipo": "carro"
}
```

Esto permite buscar, verificar existencia o actualizar un registro en tiempo constante a través de su clave, sin necesidad de recorrer todo el diccionario (excepto en los casos donde se filtra por un campo distinto a la clave, como el historial de citas de un cliente).

## Persistencia

Los cuatro módulos usan el mismo esquema de persistencia:

- **Carga:** al importar el módulo (`import clientes`, `import vehiculos`, etc.), se ejecuta automáticamente `cargar<Entidad>()`, que lee el archivo `.json` correspondiente con `json.load()` y llena el diccionario en memoria. Si el archivo no existe o está corrupto, el diccionario simplemente arranca vacío.
- **Guardado:** cada vez que se registra o modifica un elemento, se llama a `guardar<Entidad>()`, que sobrescribe el archivo completo con `json.dump()` sobre el diccionario en memoria.

Con este esquema, el archivo `.json` siempre refleja el estado completo y actual de la colección, y los datos persisten entre distintas ejecuciones del programa.

## Validaciones

**Clientes**
- Nombre: solo letras y espacios.
- Edad: numérica, entre 16 y 60 años.
- Documento: solo dígitos, entre 7 y 10 caracteres, y no puede repetirse.
- Teléfono: 10 dígitos numéricos y no puede repetirse con el de otro cliente.
- Tipo de vehículo aplicable: carro, moto, o ambos.

**Instructores**
- Nombre: solo letras y espacios.
- Documento: solo dígitos, entre 8 y 10 caracteres, y no puede repetirse.
- Teléfono: 10 dígitos numéricos.
- Especialidad: carro, moto, o ambos.

**Vehículos**
- Placa de carro: formato `ABC123` (3 letras + 3 dígitos).
- Placa de moto: formato `ABC12D` (3 letras + 2 dígitos + 1 letra).
- La placa no puede repetirse.

**Citas**
- Cliente, instructor y vehículo deben existir previamente en sus respectivos registros.
- El tipo de vehículo debe ser compatible con lo que aplica el cliente y con la especialidad del instructor.
- Fecha en formato `DD/MM/AAAA`, validada como fecha real.
- Hora en formato `HH:MM` (24h), restringida al horario de 7:00 a.m. a 6:00 p.m.
- Duración entre 30 y 240 minutos.
- No se permite programar una cita en una fecha/hora ya pasada.
- No se permite que un mismo instructor o un mismo vehículo tengan dos citas que se solapen en el tiempo.

## Funcionalidades por opción del menú

1. **Registrar cliente / instructor / vehículo:** ciclo de registro que permite ingresar uno o varios registros seguidos, mostrando al final el total registrado en esa sesión.
2. **Programar cita:** solicita documento del cliente, placa del vehículo y documento del instructor (mostrando en cada paso la lista de registrados), valida la compatibilidad entre ellos, pide fecha, hora y duración, y valida que no haya cruces de horario.
3. **Consultar citas programadas:** busca una cita por su id y muestra sus datos completos.
4. **Registrar asistencia y observaciones:** busca una cita existente por id y actualiza si el cliente asistió y las observaciones de la práctica.
5. **Consultar historial de prácticas:** busca todas las citas asociadas a un documento de cliente y las lista con su fecha, hora y estado de asistencia.