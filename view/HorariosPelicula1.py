from PyQt5 import QtCore, QtGui, QtWidgets
from view.Pelicula1.P1Funcion1 import Ui_P1Funcion1
from view.Pelicula1.P1Funcion2 import Ui_P1Funcion2
from view.Pelicula1.P1Funcion3 import Ui_P1Funcion3
from view.Pelicula1.P1Funcion4 import Ui_P1Funcion4
from view.Pelicula1.P1Funcion5 import Ui_P1Funcion5
from view.Pelicula1.P1Funcion6 import Ui_P1Funcion6
from view.Pelicula1.P1Funcion7 import Ui_P1Funcion7
from view.RecaudacionP1 import Ui_VentanaRecaudacion

class Ui_HorariosPelicula1(object):
    def setupUi(self, HorariosPelicula1):
        HorariosPelicula1.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(HorariosPelicula1)
        self.centralwidget.setObjectName("centralwidget")

        ### INTERFAZ TEXTO TITULOS DE HORARIOS Y PELICULA ###
        self.TituloHorario = QtWidgets.QLabel(self.centralwidget)
        self.TituloHorario.setGeometry(QtCore.QRect(160, 30, 500, 40))
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
        self.BotonP1F1 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP1F1.setGeometry(QtCore.QRect(100, 180, 86, 27))
        self.BotonP1F2 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP1F2.setGeometry(QtCore.QRect(100, 240, 86, 27))
        self.BotonP1F3 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP1F3.setGeometry(QtCore.QRect(365, 180, 86, 27))
        self.BotonP1F4 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP1F4.setGeometry(QtCore.QRect(365, 240, 86, 27))
        self.BotonP1F5 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP1F5.setGeometry(QtCore.QRect(365, 300, 86, 27))
        self.BotonP1F6 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP1F6.setGeometry(QtCore.QRect(630, 180, 86, 27))
        self.BotonP1F7 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonP1F7.setGeometry(QtCore.QRect(630, 240, 86, 27))
        
        ### INTEFAZ BOTONES COMPRA Y VENTA ###
        self.BotonVolver = QtWidgets.QPushButton(self.centralwidget)
        self.BotonVolver.setGeometry(QtCore.QRect(20, 540, 120, 40))
        self.BotonRecaudacion = QtWidgets.QPushButton(self.centralwidget)
        self.BotonRecaudacion.setGeometry(QtCore.QRect(660, 540, 120, 40))

        ### INTERFAZ TEXTO F1 - F7 ###
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
        self.TextoF7 = QtWidgets.QLabel(self.centralwidget)
        self.TextoF7.setGeometry(QtCore.QRect(605, 240, 27, 27))
        self.TextoF7.setTextFormat(QtCore.Qt.RichText)

        HorariosPelicula1.setCentralWidget(self.centralwidget)

        self.definirTextos(HorariosPelicula1)
        
    ### - CONTROLADOR - ###
    
        self.BotonP1F1.clicked.connect(self.onActionP1F1)
        self.BotonP1F2.clicked.connect(self.onActionP1F2)
        self.BotonP1F3.clicked.connect(self.onActionP1F3)
        self.BotonP1F4.clicked.connect(self.onActionP1F4)
        self.BotonP1F5.clicked.connect(self.onActionP1F5)
        self.BotonP1F6.clicked.connect(self.onActionP1F6)
        self.BotonP1F7.clicked.connect(self.onActionP1F7)

        ### BOTON VOLVER Y COMPRAR ###
        self.BotonVolver.clicked.connect(HorariosPelicula1.close) #Boton para cerrar la ventana
        self.BotonRecaudacion.clicked.connect(self.onActionRecaudar)


    def onActionRecaudar(self):
        self.ventanaRecaudacionP1 = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaRecaudacion()
        self.ui.setupUi(self.ventanaRecaudacionP1)
        self.ventanaRecaudacionP1.show()
        

    def onActionP1F1(self):
        self.ventanaP1F1 = QtWidgets.QMainWindow()
        self.ui = Ui_P1Funcion1()
        self.ui.setupUi(self.ventanaP1F1)
        self.ventanaP1F1.show()
        
    def onActionP1F2(self):
        self.ventanaP1F2 = QtWidgets.QMainWindow()
        self.ui = Ui_P1Funcion2()
        self.ui.setupUi(self.ventanaP1F2)
        self.ventanaP1F2.show()

    def onActionP1F3(self):
        self.ventanaP1F3 = QtWidgets.QMainWindow()
        self.ui = Ui_P1Funcion3()
        self.ui.setupUi(self.ventanaP1F3)
        self.ventanaP1F3.show()

    def onActionP1F4(self):
        self.ventanaP1F4 = QtWidgets.QMainWindow()
        self.ui = Ui_P1Funcion4()
        self.ui.setupUi(self.ventanaP1F4)
        self.ventanaP1F4.show()

    def onActionP1F5(self):
        self.ventanaP1F5 = QtWidgets.QMainWindow()
        self.ui = Ui_P1Funcion5()
        self.ui.setupUi(self.ventanaP1F5)
        self.ventanaP1F5.show()

    def onActionP1F6(self):
        self.ventanaP1F6 = QtWidgets.QMainWindow()
        self.ui = Ui_P1Funcion6()
        self.ui.setupUi(self.ventanaP1F6)
        self.ventanaP1F6.show()

    def onActionP1F7(self):
        self.ventanaP1F7 = QtWidgets.QMainWindow()
        self.ui = Ui_P1Funcion7()
        self.ui.setupUi(self.ventanaP1F7)
        self.ventanaP1F7.show()

    def definirTextos(self, HorariosPelicula1):
        textoEnriquecido = QtCore.QCoreApplication.translate
        HorariosPelicula1.setWindowTitle("Ventana Horarios Wall-E - Cinema PM")
        self.TituloHorario.setText(textoEnriquecido("HorariosPelicula1", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">HORARIOS WALL-E</span></p></body></html>"))
        self.TituloMatine.setText(textoEnriquecido("HorariosPelicula1", "<html><head/><body><p><span style=\" font-size:12pt;\">Matiné</span></p></body></html>"))
        self.TituloVermut.setText(textoEnriquecido("HorariosPelicula1", "<html><head/><body><p><span style=\" font-size:12pt;\">Vermut</span></p><p><br/></p></body></html>"))
        self.TituloVespertino.setText(textoEnriquecido("HorariosPelicula1", "<html><head/><body><p><span style=\" font-size:12pt;\">Vespertino</span></p><p><br/></p></body></html>"))
        self.BotonP1F1.setText("08:00 - 09:30")
        self.BotonP1F2.setText("10:00 - 11:30")
        self.BotonP1F3.setText("13:00 - 14:30")
        self.BotonP1F4.setText("15:00 - 16:30")
        self.BotonP1F5.setText("17:00 - 18:30")
        self.BotonP1F6.setText("20:00 - 21:30")
        self.BotonP1F7.setText("22:00 - 23:30")
        self.TextoF1.setText("F1")
        self.TextoF2.setText("F2")
        self.TextoF3.setText("F3")
        self.TextoF4.setText("F4")
        self.TextoF5.setText("F5")
        self.TextoF6.setText("F6")
        self.TextoF7.setText("F7")
        self.BotonVolver.setText("Volver")
        self.BotonRecaudacion.setText("Recaudación Wall-E")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HorariosPelicula1 = QtWidgets.QMainWindow()
    ui = Ui_HorariosPelicula1()
    ui.setupUi(HorariosPelicula1)
    HorariosPelicula1.show()
    sys.exit(app.exec_())
