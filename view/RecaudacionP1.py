from PyQt5 import QtCore, QtGui, QtWidgets
ventasTotalesP1=0

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
        from view.Pelicula1.P1Funcion1 import ventasTotalesP1F1
        from view.Pelicula1.P1Funcion2 import ventasTotalesP1F2
        from view.Pelicula1.P1Funcion3 import ventasTotalesP1F3
        from view.Pelicula1.P1Funcion4 import ventasTotalesP1F4
        from view.Pelicula1.P1Funcion5 import ventasTotalesP1F5
        from view.Pelicula1.P1Funcion6 import ventasTotalesP1F6
        from view.Pelicula1.P1Funcion7 import ventasTotalesP1F7
        global ventasTotalesP1
        ventasTotalesP1=ventasTotalesP1F1+ventasTotalesP1F2+ventasTotalesP1F3+ventasTotalesP1F4+ventasTotalesP1F5+ventasTotalesP1F6+ventasTotalesP1F7

    def definirTextos(self, VentanaRecaudacion):
        global ventasTotalesP1
        textoEnriquecido = QtCore.QCoreApplication.translate
        VentanaRecaudacion.setWindowTitle("Recaudación Wall-E - Cinema PM")
        self.TextoRecaudacion.setText(textoEnriquecido("VentanaRecaudacion", "<span style=\" font-size:11pt; font-weight:550;\">En la pelicula Wall-E se han recaudado: $" + str(ventasTotalesP1)))
        self.BotonVolver.setText("Volver")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaRecaudacion = QtWidgets.QMainWindow()
    ui = Ui_VentanaRecaudacion()
    ui.setupUi(VentanaRecaudacion)
    VentanaRecaudacion.show()
    sys.exit(app.exec_())