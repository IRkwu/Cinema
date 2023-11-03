from PyQt5 import QtCore, QtGui, QtWidgets
ventasTotalesP2=0

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

        self.recaudacion()
        self.definirTextos(VentanaRecaudacion)

        self.BotonVolver.clicked.connect(VentanaRecaudacion.close) #Boton para cerrar la ventana


    def recaudacion(self):
        from view.Pelicula2.P2Funcion1 import ventasTotalesP2F1
        from view.Pelicula2.P2Funcion2 import ventasTotalesP2F2
        from view.Pelicula2.P2Funcion3 import ventasTotalesP2F3
        from view.Pelicula2.P2Funcion4 import ventasTotalesP2F4
        from view.Pelicula2.P2Funcion5 import ventasTotalesP2F5
        from view.Pelicula2.P2Funcion6 import ventasTotalesP2F6
        global ventasTotalesP2
        ventasTotalesP2=ventasTotalesP2F1+ventasTotalesP2F2+ventasTotalesP2F3+ventasTotalesP2F4+ventasTotalesP2F5+ventasTotalesP2F6

    def definirTextos(self, VentanaRecaudacion):
        global ventasTotalesP2
        textoEnriquecido = QtCore.QCoreApplication.translate
        VentanaRecaudacion.setWindowTitle("Recaudación Cars - Cinema PM")
        self.TextoRecaudacion.setText(textoEnriquecido("VentanaRecaudacion", "<span style=\" font-size:11pt; font-weight:550;\">En la pelicula Cars se han recaudado: $" + str(ventasTotalesP2)))
        self.BotonVolver.setText("Volver")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaRecaudacion = QtWidgets.QMainWindow()
    ui = Ui_VentanaRecaudacion()
    ui.setupUi(VentanaRecaudacion)
    VentanaRecaudacion.show()
    sys.exit(app.exec_())