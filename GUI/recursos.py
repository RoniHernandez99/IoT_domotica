class App_Principal():
    ARCHIVO_ESTADOS_SENSORES="CUERPO/RECURSOS/DATOS/estadosSensores.txt"
    SONIDO_INCENDIO="CUERPO/RECURSOS/SONIDOS_SISTEMA/fuego_detectado.wav"

    ARDUINO_NANO_EXTENSION="COM7"
    BLUETOOTH_HC05="COM5"

    ICONO_APLICACION=":/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/RoniHernandez99_IoT_domotica_128px.ico"
    NOMBRE_APLICACION="RoniHernandez99/IoT_domotica"
    IMAGEN_SPLASH_SCREEN=":/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/RoniHernandez99_IoT_domotica_512px.png"


class App_Alarmas():
    NOMBRE_BASE_DATOS_ALARMAS="CUERPO/RECURSOS/DATOS/BaseDatosAlarma.db"

    CARPETA_MUSICA="CUERPO/RECURSOS/MUSICA/"
    CARPETA_MUSICA_DEFAULT="DEFAULT/"
    CARPETA_MUSICA_MIA="MIA/"
    
    NOMBRE_SONIDO_NULL="SIN MUSICA"
    AUDIO_YA_DESPIERTA="CUERPO/RECURSOS/SONIDOS_SISTEMA/hora_despertar.wav"
    AUDIO_IR_DORMIR="CUERPO/RECURSOS/SONIDOS_SISTEMA/hora_dormir.wav"
    AUDIO_HAZ_DEBERES="CUERPO/RECURSOS/SONIDOS_SISTEMA/hora_deberes.wav"


class App_Notas():
    ARCHIVO_DEBERES="CUERPO/RECURSOS/DATOS/deberes.txt"
    SEPARADOR_DEBERES='^'



from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon

#class HuellaAplicacion(QtCore.QObject):
class HuellaAplicacion(QtCore.QObject):
    NOMBRE_APLICACION=App_Principal.NOMBRE_APLICACION
    ICONO_APLICACION=App_Principal.ICONO_APLICACION

    def __init__(self):
        #NO USAMOS EL CONSTRUCTOR DEL PADRE POR LO TANTO NO HACEMOS SUS CONFIGURACIONES DEFAULT
        self.dejarHuella()
    

    def dejarHuella(self):
        self.setWindowTitle(self.NOMBRE_APLICACION)
        self.setWindowIcon( QIcon(self.ICONO_APLICACION) )  


