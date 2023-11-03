from PyQt5 import QtCore, QtGui, QtWidgets
ventasTotalesP3=0

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
        from view.Pelicula3.P3Funcion1 import ventasTotalesP3F1
        from view.Pelicula3.P3Funcion2 import ventasTotalesP3F2
        from view.Pelicula3.P3Funcion3 import ventasTotalesP3F3
        from view.Pelicula3.P3Funcion4 import ventasTotalesP3F4
        from view.Pelicula3.P3Funcion5 import ventasTotalesP3F5
        from view.Pelicula3.P3Funcion6 import ventasTotalesP3F6
        global ventasTotalesP3
        ventasTotalesP3=ventasTotalesP3F1+ventasTotalesP3F2+ventasTotalesP3F3+ventasTotalesP3F4+ventasTotalesP3F5+ventasTotalesP3F6

    def definirTextos(self, VentanaRecaudacion):
        global ventasTotalesP3
        textoEnriquecido = QtCore.QCoreApplication.translate
        VentanaRecaudacion.setWindowTitle("Recaudación UP - Cinema PM")
        self.TextoRecaudacion.setText(textoEnriquecido("VentanaRecaudacion", "<span style=\" font-size:11pt; font-weight:550;\">En la pelicula UP se han recaudado: $" + str(ventasTotalesP3)))
        self.BotonVolver.setText("Volver")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaRecaudacion = QtWidgets.QMainWindow()
    ui = Ui_VentanaRecaudacion()
    ui.setupUi(VentanaRecaudacion)
    VentanaRecaudacion.show()
    sys.exit(app.exec_())