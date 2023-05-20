
# Declaramos las clases necesarias para el proyecto
#Clase principal
class Trashcity:
    _instance = None

    def __new__(cls, nombre):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, nombre):
        self.nombre = nombre
        self.rutas = []
        self.camiones = []
        self.centroAcopio = []

    #Metodo para agregar rutas
    def asignarRuta(self, ruta):
        self.rutas.append(ruta)

    def asignarCamion(self, camion):
        self.camiones.append(camion)

    def asignarCentroAcopio(self, centroAcopio):
        self.centroAcopio.append(centroAcopio)

# Clase Camion
class Camion:
    def __init__(self, id):
        self.observers = []
        self.id = id
        self.turnos = []

    # Metodos para asignar turnos, asistentes y conductor
    def asignarTurno(self, turno):
        self.turnos.append(turno)
    def asignarConductor(self, conductor):
        self.conductor = conductor
    def asignarAsistente(self, asistente1, asistente2):
        self.asistente1 = asistente1
        self.asistente2 = asistente2

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update()

# Clase Turno
class Turno:
    def __init__(self, id, horaInicio, horaFin, ruta, carga):
        self.__id = id
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.__ruta = ruta
        self.__ubicacion = []
        self.carga = carga

    @property # Decorador para obtener el id
    def id(self):
        return self.__id

    @property # Decorador para obtener la ruta
    def ruta(self):
        return self.__ruta

    @property # Decorador para obtener la ubicacion
    def ubicacion(self):
        return self.__ubicacion

    # Metodos para asignar ruta, camion y asistentes
    def asignarUbicacion(self, puntogeografico):
        self.ubicacion.append(puntogeografico)

    def asignarCarga(self, carga):
        self.carga = carga

    # def asignarRuta(self, ruta):
    #     self.ruta = ruta
    # def asignarCamion(self, camion):
    #     self.camion = camion
    # def asignarAsistente(self, asistente):
    #     self.asistentes.append(asistente)

# Clase de Ubicacion
class PuntoGeografico:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud


# Clase Ruta
class Ruta:
    def __init__(self, id, nombre, puntos):
        self.id = id
        self.nombre = nombre
        self.puntos = puntos

    # Metodo para asignar puntos geograficos
    def asignarPunto(self, punto):
        self.puntos.append(punto)

# Clase Carga
class Carga:
    def __init__(self, t_vidrio, t_papel, t_plastico, t_organico, t_metal):
        self.t_vidrio = t_vidrio
        self.t_papel = t_papel
        self.t_plastico = t_plastico
        self.t_organico = t_organico
        self.t_metal = t_metal

class CargaDecorator:
    def __init__(self, carga):
        self.carga = carga
    def calcularPesoTotal(self):
        total = (
            self.carga.t_vidrio
            + self.carga.t_papel
            + self.carga.t_plastico
            + self.carga.t_organico
            + self.carga.t_metal
            )
        return total

carga = Carga(10, 20, 30, 40, 50)
decorated_carga = CargaDecorator(carga)
peso_total = decorated_carga.calcularPesoTotal()

# Clase Persona
class Persona:
    def __init__(self, nombre, id):
        self._nombre = nombre
        self._id = id

# Clases hijas de Persona
class Conductor(Persona):
    def __init__(self, nombre, id):
        super().__init__(nombre, id)

class Asistente(Persona):
    def __init__(self, nombre, id):
        super().__init__(nombre, id)

# Clase Centro de Acopio
class CentroAcopio:
    def __init__(self, nombre, direccion):
        self.tot_vidrio = 0
        self.nombre = nombre
        self.direccion = direccion
        self.camiones = []

    def asignarCamion(self, camion):
        self.camiones.append(camion)
        camion.addObserver(self)

    def update(self):
        # Realizar acciones cuando se actualiza un camión
        self.calcularReciclaje()

    # Metodo para calcular los desechos
    def calcularReciclaje(self):
        for camion in self.camiones:
            for turno in camion.turnos:

                self.tot_vidrio += turno.carga.t_vidrio

            print("El acumulado de vidrio en el camion {} es de {} kg".format(camion.id, self.tot_vidrio))
# Instanciamos las clases


# Instanciamos los puntos geograficos
punto1 = PuntoGeografico(10.0, 10.0)
punto2 = PuntoGeografico(20.0, 20.0)
punto3 = PuntoGeografico(30.0, 30.0)
punto4 = PuntoGeografico(40.0, 40.0)

# Instanciamos las rutas
ruta1 = Ruta(1, "Ruta 1", [punto1, punto2])
ruta2 = Ruta(2, "Ruta 2", [punto3, punto4])

# Instanciamos las cargas
carga1 = Carga(10, 20, 30, 40, 50)
carga2 = Carga(60, 70, 80, 90, 100)

# Instanciamos los turnos
turno1 = Turno(1, "10:00", "12:00", ruta1, carga1)
turno2 = Turno(2, "12:00", "14:00", ruta2, carga2)
turno1.asignarCarga(carga1)
turno2.asignarCarga(carga2)
turno1.asignarUbicacion(punto1)
turno1.asignarUbicacion(punto2)
turno2.asignarUbicacion(punto3)
turno2.asignarUbicacion(punto4)

# Instanciamos los conductores
juan = Conductor("Juan", 109845623)
pedro = Conductor("Pedro", 1054367891)

# Instanciamos los asistentes
maria = Asistente("Maria", 109845623)
jose = Asistente("Jose", 1054367891)
miguel = Asistente("Miguel", 1034908765)
sebastian = Asistente("Sebastian", 10213490432)

# Instanciamos los camiones
camion1 = Camion(1)
camion1.asignarTurno(turno1)
camion1.asignarTurno(turno2)
camion1.asignarConductor(juan)
camion1.asignarAsistente(maria, jose)


# Instanciamos el centro de acopio
centroAcopio1 = CentroAcopio("Centro de Acopio 1", "Calle 1 # 1 - 1")
centroAcopio1.asignarCamion(camion1)


# Imprimimos los datos

print("Inicia el día en el centro de acopio {} ubicado en {}".format(centroAcopio1.nombre, centroAcopio1.direccion))
print("El camion {} tiene {} turnos".format(camion1.id, len(camion1.turnos)))


# print("La ruta del turno {} es {}".format(turno1.id, turno1.ubicacion))
for elemento, turno in zip(turno1.ubicacion, camion1.turnos):
    print("El camion {} en el turno {} pasó por el punto geografico {}, {}".format(camion1.id, turno.id, elemento.latitud, elemento.longitud))
    print("El conductor del camion {} en el turno {} es {}".format(camion1.id, turno.id, camion1.conductor._nombre))
    print("Los asistentes del camion {} en el turno {} son: Asistente1: {}, Asistente2: {} ".format(camion1.id, turno.id, camion1.asistente1._nombre, camion1.asistente2._nombre))
for camion in centroAcopio1.camiones:
    for turno in camion.turnos:
        print("El camion {} en el turno {} recolectó {} kg de vidrio, {} kg de papel, {} kg de plastico, {} kg de organico y {} kg de metal".format(camion.id, turno.id, turno.carga.t_vidrio, turno.carga.t_papel, turno.carga.t_plastico, turno.carga.t_organico, turno.carga.t_metal))
centroAcopio1.calcularReciclaje()




