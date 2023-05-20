# Parcial2_Poo
### Por Carlos López Gallardo
### Código estudiantil: 200176533
### Correo: cegallardo@uninorte.edu.co

Trash City
Descripción

Trash City es un sistema de gestión de recolección de basura en una ciudad. Permite asignar rutas, camiones, conductores, asistentes y centros de acopio. Además, realiza un seguimiento de la carga recogida en cada turno y calcula el total de vidrio reciclado en los centros de acopio.
Clases
Clase principal: Trashcity

Esta clase representa el sistema Trash City. Solo puede existir una instancia de esta clase. Tiene los siguientes atributos:

    nombre: Nombre de la ciudad.
    rutas: Lista de rutas asignadas.
    camiones: Lista de camiones asignados.
    centroAcopio: Lista de centros de acopio.

Además, cuenta con los siguientes métodos:

    asignarRuta(ruta): Asigna una ruta a la lista de rutas.
    asignarCamion(camion): Asigna un camión a la lista de camiones.
    asignarCentroAcopio(centroAcopio): Asigna un centro de acopio a la lista de centros de acopio.

Clase Camion

Esta clase representa un camión de basura. Tiene los siguientes atributos:

    observers: Lista de observadores (centros de acopio) que están pendientes de las actualizaciones del camión.
    id: Identificador del camión.
    turnos: Lista de turnos asignados al camión.

Además, cuenta con los siguientes métodos:

    asignarTurno(turno): Asigna un turno a la lista de turnos.
    asignarConductor(conductor): Asigna un conductor al camión.
    asignarAsistente(asistente1, asistente2): Asigna dos asistentes al camión.
    addObserver(observer): Agrega un observador (centro de acopio) a la lista de observadores.
    removeObserver(observer): Elimina un observador (centro de acopio) de la lista de observadores.
    notifyObservers(): Notifica a los observadores (centros de acopio) cuando se actualiza el camión.

Clase Turno

Esta clase representa un turno de recolección de basura. Tiene los siguientes atributos:

    id: Identificador del turno.
    horaInicio: Hora de inicio del turno.
    horaFin: Hora de fin del turno.
    ruta: Ruta asignada al turno.
    ubicacion: Lista de ubicaciones visitadas durante el turno.
    carga: Carga recolectada durante el turno.

Además, cuenta con los siguientes métodos:

    asignarUbicacion(puntogeografico): Asigna una ubicación a la lista de ubicaciones.
    asignarCarga(carga): Asigna una carga al turno.

Clase PuntoGeografico

Esta clase representa un punto geográfico con coordenadas de latitud y longitud. Tiene los siguientes atributos:

    latitud: Latitud del punto.
    longitud: Longitud del punto.

Clase Ruta

Esta clase representa una ruta de recolección de basura. Tiene los siguientes atributos:

    id: Identificador de la ruta.
    nombre: Nombre de la ruta.
    puntos: Lista de puntos geográficos que conforman la ruta.

Además, cuenta con el siguiente método:

    asignarPunto(punto): Asigna un punto geográfico a la lista de puntos.

Clase Carga

Esta clase representa la carga recolectada durante un turno. Tiene los siguientes atributos:

    t_vidrio: Cantidad de vidrio recolectado.
    t_papel: Cantidad de papel recolectado.
    t_plastico: Cantidad de plástico recolectado.
    t_organico: Cantidad de residuos orgánicos recolectados.
    t_metal: Cantidad de metal recolectado.

Clase CargaDecorator

Esta clase es un decorador para la clase Carga y permite calcular el peso total de la carga recolectada. Tiene un atributo carga que es una instancia de la clase Carga. Cuenta con el método calcularPesoTotal() para calcular el peso total de la carga.
Clase Persona

Esta clase representa una persona y tiene los siguientes atributos:

    _nombre: Nombre de la persona.
    _id: Identificador de la persona.

Clase Conductor y Asistente

Estas clases son subclases de la clase Persona y representan un conductor y un asistente, respectivamente. Heredan los atributos y métodos de la clase Persona.
Clase CentroAcopio

Esta clase representa un centro de acopio de basura. Tiene los siguientes atributos:

    tot_vidrio: Total acumulado de vidrio reciclado en el centro de acopio.
    nombre: Nombre del centro de acopio.
    direccion: Dirección del centro de acopio.
    camiones: Lista de camiones asignados al centro de acopio.

Además, cuenta con los siguientes métodos:

    asignarCamion(camion): Asigna un camión al centro de acopio y agrega el centro de acopio como observador del camión.
    update(): Actualiza el centro de acopio cuando se actualiza un camión. Calcula el reciclaje acumulado de vidrio.
    calcularReciclaje(): Calcula el reciclaje acumulado de vidrio en los camiones asignados al centro de acopio.
