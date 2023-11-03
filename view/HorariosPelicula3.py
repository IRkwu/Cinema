from PyQt5 import QtCore, QtGui, QtWidgets
from view.Pelicula3.P3Funcion1 import Ui_P3Funcion1
from view.Pelicula3.P3Funcion2 import Ui_P3Funcion2
from view.Pelicula3.P3Funcion3 import Ui_P3Funcion3
from view.Pelicula3.P3Funcion4 import Ui_P3Funcion4
from view.Pelicula3.P3Funcion5 import Ui_P3Funcion5
from view.Pelicula3.P3Funcion6 import Ui_P3Funcion6
from view.RecaudacionP3 import Ui_VentanaRecaudacion

class Ui_HorariosPelicula3(object):
    def setupUi(self, HorariosPelicula3):
        HorariosPelicula3.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(HorariosPelicula3)
        self.centralwidget.setObjectName("centralwidget")
       

        ### INTERFAZ TEXTO TITULOS DE HORARIOS Y PELICULA ###
        self.TituloHorario = QtWidgets.QLabel(self.centralwidget)
        self.TituloHorario.setGeometry(QtCore.QRect(246, 30, 300, 40))
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
        self.BotonP3F1 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP3F1.setGeometry(QtCore.QRect(100, 180, 86, 27))
        self.BotonP3F2 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP3F2.setGeometry(QtCore.QRect(100, 240, 86, 27))
        self.BotonP3F3 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP3F3.setGeometry(QtCore.QRect(365, 180, 86, 27))
        self.BotonP3F4 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP3F4.setGeometry(QtCore.QRect(630, 180, 86, 27))
        self.BotonP3F5 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP3F5.setGeometry(QtCore.QRect(630, 240, 86, 27))
        self.BotonP3F6 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP3F6.setGeometry(QtCore.QRect(630, 300, 86, 27))

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
        self.TextoF4.setGeometry(QtCore.QRect(605, 180, 27, 27))
        self.TextoF4.setTextFormat(QtCore.Qt.RichText)
        self.TextoF5 = QtWidgets.QLabel(self.centralwidget)
        self.TextoF5.setGeometry(QtCore.QRect(605, 240, 27, 27))
        self.TextoF5.setTextFormat(QtCore.Qt.RichText)
        self.TextoF6 = QtWidgets.QLabel(self.centralwidget)
        self.TextoF6.setGeometry(QtCore.QRect(605, 300, 27, 27))
        self.TextoF6.setTextFormat(QtCore.Qt.RichText)

        HorariosPelicula3.setCentralWidget(self.centralwidget)

        self.definirTextos(HorariosPelicula3)

        ### - CONTROLADOR - ###
    
        self.BotonP3F1.clicked.connect(self.onActionP3F1)
        self.BotonP3F2.clicked.connect(self.onActionP3F2)
        self.BotonP3F3.clicked.connect(self.onActionP3F3)
        self.BotonP3F4.clicked.connect(self.onActionP3F4)
        self.BotonP3F5.clicked.connect(self.onActionP3F5)
        self.BotonP3F6.clicked.connect(self.onActionP3F6)

        ### BOTON VOLVER Y COMPRAR ###
        self.BotonVolver.clicked.connect(HorariosPelicula3.close) #Boton para cerrar la ventana
        self.BotonRecaudacion.clicked.connect(self.onActionRecaudar)

    def onActionRecaudar(self):
        self.ventanaRecaudacionP3 = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaRecaudacion()
        self.ui.setupUi(self.ventanaRecaudacionP3)
        self.ventanaRecaudacionP3.show()
        
    def onActionP3F1(self):
        self.ventanaP3F1 = QtWidgets.QMainWindow()
        self.ui = Ui_P3Funcion1()
        self.ui.setupUi(self.ventanaP3F1)
        self.ventanaP3F1.show()
        
    def onActionP3F2(self):
        self.ventanaP3F2 = QtWidgets.QMainWindow()
        self.ui = Ui_P3Funcion2()
        self.ui.setupUi(self.ventanaP3F2)
        self.ventanaP3F2.show()

    def onActionP3F3(self):
        self.ventanaP3F3 = QtWidgets.QMainWindow()
        self.ui = Ui_P3Funcion3()
        self.ui.setupUi(self.ventanaP3F3)
        self.ventanaP3F3.show()

    def onActionP3F4(self):
        self.ventanaP3F4 = QtWidgets.QMainWindow()
        self.ui = Ui_P3Funcion4()
        self.ui.setupUi(self.ventanaP3F4)
        self.ventanaP3F4.show()

    def onActionP3F5(self):
        self.ventanaP3F5 = QtWidgets.QMainWindow()
        self.ui = Ui_P3Funcion5()
        self.ui.setupUi(self.ventanaP3F5)
        self.ventanaP3F5.show()

    def onActionP3F6(self):
        self.ventanaP3F6 = QtWidgets.QMainWindow()
        self.ui = Ui_P3Funcion6()
        self.ui.setupUi(self.ventanaP3F6)
        self.ventanaP3F6.show()

    def definirTextos(self, HorariosPelicula3):
        textoEnriquecido = QtCore.QCoreApplication.translate
        HorariosPelicula3.setWindowTitle("Ventana Horarios UP - Cinema PM")
        self.TituloHorario.setText(textoEnriquecido("HorariosPelicula3", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">HORARIOS UP</span></p></body></html>"))
        self.TituloMatine.setText(textoEnriquecido("HorariosPelicula3", "<html><head/><body><p><span style=\" font-size:12pt;\">Matiné</span></p></body></html>"))
        self.TituloVermut.setText(textoEnriquecido("HorariosPelicula3", "<html><head/><body><p><span style=\" font-size:12pt;\">Vermut</span></p><p><br/></p></body></html>"))
        self.TituloVespertino.setText(textoEnriquecido("HorariosPelicula3", "<html><head/><body><p><span style=\" font-size:12pt;\">Vespertino</span></p><p><br/></p></body></html>"))
        self.BotonP3F1.setText("08:00 - 09:45")
        self.BotonP3F2.setText("10:00 - 11:45")
        self.BotonP3F3.setText("15:00 - 16:45")
        self.BotonP3F4.setText("20:00 - 21:45")
        self.BotonP3F5.setText("22:00 - 23:45")
        self.BotonP3F6.setText("00:00 - 01:45")
        self.TextoF1.setText("F1")
        self.TextoF2.setText("F2")
        self.TextoF3.setText("F3")
        self.TextoF4.setText("F4")
        self.TextoF5.setText("F5")
        self.TextoF6.setText("F6")
        self.BotonVolver.setText("Volver")
        self.BotonRecaudacion.setText("Recaudación UP")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HorariosPelicula3 = QtWidgets.QMainWindow()
    ui = Ui_HorariosPelicula3()
    ui.setupUi(HorariosPelicula3)
    HorariosPelicula3.show()
    sys.exit(app.exec_())
