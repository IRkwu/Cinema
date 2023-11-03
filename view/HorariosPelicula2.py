from PyQt5 import QtCore, QtGui, QtWidgets
from view.Pelicula2.P2Funcion1 import Ui_P2Funcion1
from view.Pelicula2.P2Funcion2 import Ui_P2Funcion2
from view.Pelicula2.P2Funcion3 import Ui_P2Funcion3
from view.Pelicula2.P2Funcion4 import Ui_P2Funcion4
from view.Pelicula2.P2Funcion5 import Ui_P2Funcion5
from view.Pelicula2.P2Funcion6 import Ui_P2Funcion6
from view.RecaudacionP2 import Ui_VentanaRecaudacion


class Ui_HorariosPelicula2(object):
    def setupUi(self, HorariosPelicula2):
        HorariosPelicula2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(HorariosPelicula2)
        self.centralwidget.setObjectName("centralwidget")

        ### INTERFAZ TEXTO TITULOS DE HORARIOS Y PELICULA ###
        self.TituloHorario = QtWidgets.QLabel(self.centralwidget)
        self.TituloHorario.setGeometry(QtCore.QRect(225, 30, 350, 40))
        self.TituloHorario.setTextFormat(QtCore.Qt.RichText)
        self.TituloHorario.setAlignment(QtCore.Qt.AlignCenter)
        self.TituloMatine = QtWidgets.QLabel(self.centralwidget)
        self.TituloMatine.setGeometry(QtCore.QRect(100, 120, 80, 20))
        self.TituloMatine.setTextFormat(QtCore.Qt.RichText)
        self.TituloMatine.setAlignment(QtCore.Qt.AlignCenter)
        self.TituloVermut = QtWidgets.QLabel(self.centralwidget)
        self.TituloVermut.setGeometry(QtCore.QRect(365, 120, 80, 20))
        self.TituloVermut.setTextFormat(QtCore.Qt.RichText)
        self.TituloVermut.setAlignment(QtCore.Qt.AlignCenter)
        self.TituloVespertino = QtWidgets.QLabel(self.centralwidget)
        self.TituloVespertino.setGeometry(QtCore.QRect(630, 120, 80, 20))
        self.TituloVespertino.setTextFormat(QtCore.Qt.RichText)
        self.TituloVespertino.setAlignment(QtCore.Qt.AlignCenter)

        ### INTERFAZ BOTONES PARA IR AL MENU DE LAS FUNCIONES DISPONIBLES ###
        self.BotonP2F1 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP2F1.setGeometry(QtCore.QRect(100, 180, 86, 27))
        self.BotonP2F2 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP2F2.setGeometry(QtCore.QRect(100, 240, 86, 27))
        self.BotonP2F3 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP2F3.setGeometry(QtCore.QRect(365, 180, 86, 27))
        self.BotonP2F4 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP2F4.setGeometry(QtCore.QRect(365, 240, 86, 27))
        self.BotonP2F5 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP2F5.setGeometry(QtCore.QRect(365, 300, 86, 27))
        self.BotonP2F6 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP2F6.setGeometry(QtCore.QRect(630, 180, 86, 27))

        ### INTEFAZ BOTONES COMPRA Y VENTA ###
        self.BotonVolver = QtWidgets.QPushButton(self.centralwidget)
        self.BotonVolver.setGeometry(QtCore.QRect(20, 540, 120, 40))
        self.BotonRecaudacion = QtWidgets.QPushButton(self.centralwidget)
        self.BotonRecaudacion.setGeometry(QtCore.QRect(660, 540, 120, 40))

        ### INTERFAZ TEXTO F1 - F6 ###
        self.TextoF1 = QtWidgets.QLabel(self.centralwidget)
        self.TextoF1.setGeometry(QtCore.QRect(75, 180, 27, 27))
        self.TextoF1.setTextFormat(QtCore.Qt.RichText)
        self.TextoF2 = QtWidgets.QLabel(self.centralwidget)
        self.TextoF2.setGeometry(QtCore.QRect(75, 240, 27, 27))
        self.TextoF2.setTextFormat(QtCore.Qt.RichText)
        self.TextoF3 = QtWidgets.QLabel(self.centralwidget)
        self.TextoF3.setGeometry(QtCore.QRect(340, 180, 27, 27))
        self.TextoF3.setTextFormat(QtCore.Qt.RichText)
        self.TextoF4 = QtWidgets.QLabel(self.centralwidget)
        self.TextoF4.setGeometry(QtCore.QRect(340, 240, 27, 27))
        self.TextoF4.setTextFormat(QtCore.Qt.RichText)
        self.TextoF5 = QtWidgets.QLabel(self.centralwidget)
        self.TextoF5.setGeometry(QtCore.QRect(340, 300, 27, 27))
        self.TextoF5.setTextFormat(QtCore.Qt.RichText)
        self.TextoF6 = QtWidgets.QLabel(self.centralwidget)
        self.TextoF6.setGeometry(QtCore.QRect(605, 180, 27, 27))
        self.TextoF6.setTextFormat(QtCore.Qt.RichText)

        HorariosPelicula2.setCentralWidget(self.centralwidget)
        
        self.definirTextos(HorariosPelicula2)

    ### - CONTROLADOR - ###
    
        self.BotonP2F1.clicked.connect(self.onActionP2F1)
        self.BotonP2F2.clicked.connect(self.onActionP2F2)
        self.BotonP2F3.clicked.connect(self.onActionP2F3)
        self.BotonP2F4.clicked.connect(self.onActionP2F4)
        self.BotonP2F5.clicked.connect(self.onActionP2F5)
        self.BotonP2F6.clicked.connect(self.onActionP2F6)

        ### BOTON VOLVER Y COMPRAR ###
        self.BotonVolver.clicked.connect(HorariosPelicula2.close) #Boton para cerrar la ventana
        self.BotonRecaudacion.clicked.connect(self.onActionRecaudar)

    def onActionRecaudar(self):
        self.ventanaRecaudacionP2 = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaRecaudacion()
        self.ui.setupUi(self.ventanaRecaudacionP2)
        self.ventanaRecaudacionP2.show()
        
    def onActionP2F1(self):
        self.ventanaP2F1 = QtWidgets.QMainWindow()
        self.ui = Ui_P2Funcion1()
        self.ui.setupUi(self.ventanaP2F1)
        self.ventanaP2F1.show()
        
    def onActionP2F2(self):
        self.ventanaP2F2 = QtWidgets.QMainWindow()
        self.ui = Ui_P2Funcion2()
        self.ui.setupUi(self.ventanaP2F2)
        self.ventanaP2F2.show()

    def onActionP2F3(self):
        self.ventanaP2F3 = QtWidgets.QMainWindow()
        self.ui = Ui_P2Funcion3()
        self.ui.setupUi(self.ventanaP2F3)
        self.ventanaP2F3.show()

    def onActionP2F4(self):
        self.ventanaP2F4 = QtWidgets.QMainWindow()
        self.ui = Ui_P2Funcion4()
        self.ui.setupUi(self.ventanaP2F4)
        self.ventanaP2F4.show()

    def onActionP2F5(self):
        self.ventanaP2F5 = QtWidgets.QMainWindow()
        self.ui = Ui_P2Funcion5()
        self.ui.setupUi(self.ventanaP2F5)
        self.ventanaP2F5.show()

    def onActionP2F6(self):
        self.ventanaP2F6 = QtWidgets.QMainWindow()
        self.ui = Ui_P2Funcion6()
        self.ui.setupUi(self.ventanaP2F6)
        self.ventanaP2F6.show()

    def definirTextos(self, HorariosPelicula2):
        textoEnriquecido = QtCore.QCoreApplication.translate
        HorariosPelicula2.setWindowTitle("Ventana Horarios Cars - Cinema PM")
        self.TituloHorario.setText(textoEnriquecido("HorariosPelicula2", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">HORARIOS CARS</span></p></body></html>"))
        self.TituloMatine.setText(textoEnriquecido("HorariosPelicula2", "<html><head/><body><p><span style=\" font-size:12pt;\">Matiné</span></p></body></html>"))
        self.TituloVermut.setText(textoEnriquecido("HorariosPelicula2", "<html><head/><body><p><span style=\" font-size:12pt;\">Vermut</span></p><p><br/></p></body></html>"))
        self.TituloVespertino.setText(textoEnriquecido("HorariosPelicula2", "<html><head/><body><p><span style=\" font-size:12pt;\">Vespertino</span></p><p><br/></p></body></html>"))
        self.BotonP2F1.setText("08:30 - 10:00")
        self.BotonP2F2.setText("10:30 - 12:00")
        self.BotonP2F3.setText("13:30 - 15:00")
        self.BotonP2F4.setText("15:30 - 17:00")
        self.BotonP2F5.setText("17:30 - 19:00")
        self.BotonP2F6.setText("21:00 - 22:30")
        self.TextoF1.setText("F1")
        self.TextoF2.setText("F2")
        self.TextoF3.setText("F3")
        self.TextoF4.setText("F4")
        self.TextoF5.setText("F5")
        self.TextoF6.setText("F6")
        self.BotonVolver.setText("Volver")
        self.BotonRecaudacion.setText("Recaudación Cars")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HorariosPelicula2 = QtWidgets.QMainWindow()
    ui = Ui_HorariosPelicula2()
    ui.setupUi(HorariosPelicula2)
    HorariosPelicula2.show()
    sys.exit(app.exec_())
