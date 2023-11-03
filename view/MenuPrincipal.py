from PyQt5 import QtCore, QtGui, QtWidgets
from view.HorariosPelicula1 import Ui_HorariosPelicula1
from view.HorariosPelicula2 import Ui_HorariosPelicula2
from view.HorariosPelicula3 import Ui_HorariosPelicula3
from view.RecaudacionTotal import Ui_VentanaRecaudacion
from view.images import images


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.resize(795, 600)
        self.centralwidget = QtWidgets.QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName("centralwidget")

        ### INTERFAZ FRAMES POSTERS ###
        self.Pelicula1 = QtWidgets.QFrame(self.centralwidget)
        self.Pelicula1.setGeometry(QtCore.QRect(10, 10, 250, 400))
        self.Pelicula1.setStyleSheet("border-image: url(:/images/Pelicula1.jpg);")
        self.Pelicula1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pelicula1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Pelicula2 = QtWidgets.QFrame(self.centralwidget)
        self.Pelicula2.setGeometry(QtCore.QRect(270, 10, 250, 400))
        self.Pelicula2.setStyleSheet("border-image: url(:/images/Pelicula2.jpg);")
        self.Pelicula2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pelicula2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Pelicula3 = QtWidgets.QFrame(self.centralwidget)
        self.Pelicula3.setGeometry(QtCore.QRect(530, 10, 250, 400))
        self.Pelicula3.setStyleSheet("border-image: url(:/images/Pelicula3.jpg);")
        self.Pelicula3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pelicula3.setFrameShadow(QtWidgets.QFrame.Raised)

        ### INTERFAZ BOTONES PARA IR AL MENU DE LAS FUNCIONES DISPONIBLES ###
        self.BotonPelicula1 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonPelicula1.setGeometry(QtCore.QRect(70, 460, 140, 45))
        self.BotonPelicula2 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonPelicula2.setGeometry(QtCore.QRect(330, 460, 140, 45))
        self.BotonPelicula3 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonPelicula3.setGeometry(QtCore.QRect(580, 460, 140, 45))
        self.BotonRecaudacion = QtWidgets.QPushButton(self.centralwidget)
        self.BotonRecaudacion.setGeometry(QtCore.QRect(70, 530, 650, 45))


        VentanaPrincipal.setCentralWidget(self.centralwidget)

        self.definirTextos(VentanaPrincipal)
        
    ### - CONTROLADOR - ###
        
        self.BotonPelicula1.clicked.connect(self.onActionP1)
        self.BotonPelicula2.clicked.connect(self.onActionP2)
        self.BotonPelicula3.clicked.connect(self.onActionP3)
        self.BotonRecaudacion.clicked.connect(self.onActionRecaudar)

    def onActionRecaudar(self):
        self.ventanaRecaudacionTotal = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaRecaudacion()
        self.ui.setupUi(self.ventanaRecaudacionTotal)
        self.ventanaRecaudacionTotal.show()
        
    def onActionP1(self):
        self.ventanaHorarios = QtWidgets.QMainWindow()
        self.ui = Ui_HorariosPelicula1()
        self.ui.setupUi(self.ventanaHorarios)
        self.ventanaHorarios.show()
        
    def onActionP2(self):
        self.ventanaHorarios = QtWidgets.QMainWindow()
        self.ui = Ui_HorariosPelicula2()
        self.ui.setupUi(self.ventanaHorarios)
        self.ventanaHorarios.show()
        
    def onActionP3(self):
        self.ventanaHorarios = QtWidgets.QMainWindow()
        self.ui = Ui_HorariosPelicula3()
        self.ui.setupUi(self.ventanaHorarios)
        self.ventanaHorarios.show()

    ### FIN CONTROLADOR ###


    def definirTextos(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle("Ventana Principal - Cinema PM")
        self.BotonPelicula1.setText("Wall-E")
        self.BotonPelicula2.setText("Cars")
        self.BotonPelicula3.setText("Up")
        self.BotonRecaudacion.setText("Recaudación del día")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_VentanaPrincipal()
    ui.setupUi(VentanaPrincipal)
    VentanaPrincipal.show()
    sys.exit(app.exec_())
