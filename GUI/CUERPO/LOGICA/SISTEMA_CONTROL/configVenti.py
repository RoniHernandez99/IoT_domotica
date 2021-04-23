from PyQt5.QtWidgets import  QDialog,QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox,QButtonGroup,QDialog)
from PyQt5.QtCore import Qt, pyqtSignal,QObject
from PyQt5.QtGui import QIcon

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from  CUERPO.DISENO.SISTEMA_CONTROL.configVenti_dise import Ui_Dialog
###############################################################
#  MIS LIBRERIAS...
##############################################################

from recursos import App_Principal,HuellaAplicacion

class Dialog_configVenti(QtWidgets.QDialog, Ui_Dialog,HuellaAplicacion):
    NOMBRE_APLICACION=App_Principal.NOMBRE_APLICACION
    ICONO_APLICACION=App_Principal.ICONO_APLICACION
    senal_cambioTempPrendeVenti= pyqtSignal(float)

    def __init__(self,tempPrenderaVenti=100):
        Ui_Dialog.__init__(self)
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        self.setWindowModality(Qt.ApplicationModal)
        HuellaAplicacion.__init__(self)


        self.temp_prendeVentilador=tempPrenderaVenti #valor por default
        self.dSB_tempActVenti.setValue(tempPrenderaVenti)

        self.btn_guardarSalir.clicked.connect(self.guardarSalir)

    def guardarSalir(self):
        self.temp_prendeVentilador=self.dSB_tempActVenti.value()
        self.senal_cambioTempPrendeVenti.emit(self.temp_prendeVentilador)
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Dialog_configVenti()
    application.show()
    app.exec()
    #sys.exit(app.exec())
