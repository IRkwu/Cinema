from PyQt5 import QtCore, QtGui, QtWidgets
ventasTotales=0

class Ui_VentanaRecaudacion(object):
    def setupUi(self, VentanaRecaudacion):
        self.centralwidget = QtWidgets.QWidget(VentanaRecaudacion)
        self.centralwidget.setObjectName("centralwidget")
        VentanaRecaudacion.resize(400, 140)

        ### TEXTO RECAUDACION Y BOTON VOLVER ###
        self.TextoRecaudacion = QtWidgets.QLabel(VentanaRecaudacion)
        self.TextoRecaudacion.setGeometry(QtCore.QRect(10, 20, 391, 41))
        self.BotonVolver = QtWidgets.QPushButton(VentanaRecaudacion)
        self.BotonVolver.setGeometry(QtCore.QRect(10, 90, 100, 40))

        self.definirTextos(VentanaRecaudacion)

        self.BotonVolver.clicked.connect(VentanaRecaudacion.close) #Boton para cerrar la ventana

    def definirTextos(self, VentanaRecaudacion):
        from view.RecaudacionP1 import Ui_VentanaRecaudacion
        self.ui = Ui_VentanaRecaudacion()
        self.ui.recaudacion()
        from view.RecaudacionP2 import Ui_VentanaRecaudacion
        self.ui = Ui_VentanaRecaudacion()
        self.ui.recaudacion()
        from view.RecaudacionP3 import Ui_VentanaRecaudacion
        self.ui = Ui_VentanaRecaudacion()
        self.ui.recaudacion()
        from view.RecaudacionP1 import ventasTotalesP1
        from view.RecaudacionP2 import ventasTotalesP2
        from view.RecaudacionP3 import ventasTotalesP3
        global ventasTotales
        ventasTotales=ventasTotalesP1+ventasTotalesP2+ventasTotalesP3

        textoEnriquecido = QtCore.QCoreApplication.translate
        VentanaRecaudacion.setWindowTitle("Recaudación Peliculas -- Cinema PM")
        self.TextoRecaudacion.setText(textoEnriquecido("VentanaRecaudacion", "<span style=\" font-size:11pt; font-weight:550;\">Se han recaucado en total: $" + str(ventasTotales)))
        self.BotonVolver.setText("Volver")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaRecaudacion = QtWidgets.QMainWindow()
    ui = Ui_VentanaRecaudacion()
    ui.setupUi(VentanaRecaudacion)
    VentanaRecaudacion.show()
    sys.exit(app.exec_())