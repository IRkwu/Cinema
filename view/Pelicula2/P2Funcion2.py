from PyQt5 import QtCore, QtGui, QtWidgets

### VARIABLES GLOBALES ###
boletos_vendidos=0
ventasTotalesP2F2=0
disabled_A1=False
disabled_A2=False
disabled_A3=False
disabled_A4=False
disabled_A5=False
disabled_B1=False
disabled_B2=False
disabled_B3=False
disabled_B4=False
disabled_B5=False
disabled_C1=False
disabled_C2=False
disabled_C3=False
disabled_C4=False
disabled_C5=False
disabled_D1=False
disabled_D2=False
disabled_D3=False
disabled_D4=False
disabled_D5=False
disabled_E1=False
disabled_E2=False
disabled_E3=False
disabled_E4=False
disabled_E5=False

class Ui_P2Funcion2(object):
    def setupUi(self, P2Funcion2):
        P2Funcion2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(P2Funcion2)
        self.centralwidget.setObjectName("centralwidget")
        
        ### PANEL GRID ###
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 610, 490))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        ### INTERFAZ BOTON A1 - E5 ###
        self.A1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.A1, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.A2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.A2, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.A3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.A3, 1, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.A4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.A4, 1, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.A5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.A5, 1, 5, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.B1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.B1, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.B2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.B2, 2, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.B3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.B3, 2, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.B4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.B4, 2, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.B5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.B5, 2, 5, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.C1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.C1, 3, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.C2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.C2, 3, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.C3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.C3, 3, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.C4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.C4, 3, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.C5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.C5, 3, 5, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.D1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.D1, 4, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.D2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.D2, 4, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.D3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.D3, 4, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.D4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.D4, 4, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.D5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.D5, 4, 5, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.E1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.E1, 5, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.E2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.E2, 5, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.E3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.E3, 5, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.E4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.E4, 5, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.E5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.E5, 5, 5, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
        ### INTEFAZ BOTONES COMPRA Y VENTA ###
        self.BotonVolver = QtWidgets.QPushButton(self.centralwidget)
        self.BotonVolver.setGeometry(QtCore.QRect(20, 540, 120, 40))
        self.BotonComprar = QtWidgets.QPushButton(self.centralwidget)
        self.BotonComprar.setGeometry(QtCore.QRect(660, 540, 120, 40))
        
        ### INTERFAZ TEXTO A-E, 1-5 ###
        self.TextoA = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.TextoA, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.TextoB = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.TextoB, 2, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.TextoC = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.TextoC, 3, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.TextoD = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.TextoD, 4, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.TextoE = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.TextoE, 5, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.Texto1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.Texto1, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Texto2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.Texto2, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Texto3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.Texto3, 0, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Texto4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.Texto4, 0, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.Texto5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.Texto5, 0, 5, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        
        ### INTERFAZ INFORMACIÓN ###
        self.TextoAsientoDisponibles = QtWidgets.QLabel(self.centralwidget)
        self.TextoAsientoDisponibles.setGeometry(QtCore.QRect(620, 140, 70, 50))
        self.TextoAsientosOcupados = QtWidgets.QLabel(self.centralwidget)
        self.TextoAsientosOcupados.setGeometry(QtCore.QRect(620, 220, 70, 50))
        self.TextoBoletosVendidos = QtWidgets.QLabel(self.centralwidget)
        self.TextoBoletosVendidos.setGeometry(QtCore.QRect(620, 300, 70, 50))
        self.TextoTOTAL = QtWidgets.QLabel(self.centralwidget)
        self.TextoTOTAL.setGeometry(QtCore.QRect(620, 380, 70, 50))
        self.TextoEditable_AsientosDisponibles = QtWidgets.QTextEdit(self.centralwidget)
        self.TextoEditable_AsientosDisponibles.setGeometry(QtCore.QRect(700, 150, 70, 35))
        self.TextoEditable_AsientosOcupados = QtWidgets.QTextEdit(self.centralwidget)
        self.TextoEditable_AsientosOcupados.setGeometry(QtCore.QRect(700, 220, 70, 35))
        self.TextoEditable_BoletosVendidos = QtWidgets.QTextEdit(self.centralwidget)
        self.TextoEditable_BoletosVendidos.setGeometry(QtCore.QRect(690, 310, 70, 35))
        self.TextoEditable_TOTAL = QtWidgets.QTextEdit(self.centralwidget)
        self.TextoEditable_TOTAL.setGeometry(QtCore.QRect(670, 390, 70, 35))
        
        P2Funcion2.setCentralWidget(self.centralwidget)
        

        self.definirTextos(P2Funcion2)        
        ### INICIO CONTROLADOR ### ### INICIO CONTROLADOR ### ### INICIO CONTROLADOR ###
        
        ### MANTENER CHECKBOXES DESACTIVADAS AL HABER SIDO MARCADAS CUANDO SE REGRESE AL MENU ###
        if(self.A1.isChecked()==False or self.A2.isChecked()==False or self.A3.isChecked()==False or self.A4.isChecked()==False or self.A5.isChecked()==False or 
           self.B1.isChecked()==False or self.B2.isChecked()==False or self.B3.isChecked()==False or self.B4.isChecked()==False or self.B5.isChecked()==False or 
           self.C1.isChecked()==False or self.C2.isChecked()==False or self.C3.isChecked()==False or self.C4.isChecked()==False or self.C5.isChecked()==False or 
           self.D1.isChecked()==False or self.D2.isChecked()==False or self.D3.isChecked()==False or self.D4.isChecked()==False or self.D5.isChecked()==False or 
           self.E1.isChecked()==False or self.E2.isChecked()==False or self.E3.isChecked()==False or self.E4.isChecked()==False or self.E5.isChecked()==False):
            boletos_vendidos=0
        if(disabled_A1==True): 
            boletos_vendidos=boletos_vendidos+1
            self.A1.setChecked(True)
            self.A1.setDisabled(True)
        if(disabled_A2==True):
            boletos_vendidos=boletos_vendidos+1
            self.A2.setChecked(True)
            self.A2.setDisabled(True)
        if(disabled_A3==True):
            boletos_vendidos=boletos_vendidos+1
            self.A3.setChecked(True)
            self.A3.setDisabled(True)
        if(disabled_A4==True):
            boletos_vendidos=boletos_vendidos+1
            self.A4.setChecked(True)
            self.A4.setDisabled(True)
        if(disabled_A5==True):
            boletos_vendidos=boletos_vendidos+1
            self.A5.setChecked(True)
            self.A5.setDisabled(True)
        if(disabled_B1==True):
            boletos_vendidos=boletos_vendidos+1
            self.B1.setChecked(True)
            self.B1.setDisabled(True)
        if(disabled_B2==True):
            boletos_vendidos=boletos_vendidos+1
            self.B2.setChecked(True)
            self.B2.setDisabled(True)
        if(disabled_B3==True):
            boletos_vendidos=boletos_vendidos+1
            self.B3.setChecked(True)
            self.B3.setDisabled(True)
        if(disabled_B4==True):
            boletos_vendidos=boletos_vendidos+1
            self.B4.setChecked(True)
            self.B4.setDisabled(True)
        if(disabled_B5==True):
            boletos_vendidos=boletos_vendidos+1
            self.B5.setChecked(True)
            self.B5.setDisabled(True)
        if(disabled_C1==True):
            boletos_vendidos=boletos_vendidos+1
            self.C1.setChecked(True)
            self.C1.setDisabled(True)
        if(disabled_C2==True):
            boletos_vendidos=boletos_vendidos+1
            self.C2.setChecked(True)
            self.C2.setDisabled(True)
        if(disabled_C3==True):
            boletos_vendidos=boletos_vendidos+1
            self.C3.setChecked(True)
            self.C3.setDisabled(True)
        if(disabled_C4==True):
            boletos_vendidos=boletos_vendidos+1
            self.C4.setChecked(True)
            self.C4.setDisabled(True)
        if(disabled_C5==True):
            boletos_vendidos=boletos_vendidos+1
            self.C5.setChecked(True)
            self.C5.setDisabled(True)
        if(disabled_D1==True):
            boletos_vendidos=boletos_vendidos+1
            self.D1.setChecked(True)
            self.D1.setDisabled(True)
        if(disabled_D2==True):
            boletos_vendidos=boletos_vendidos+1
            self.D2.setChecked(True)
            self.D2.setDisabled(True)
        if(disabled_D3==True):
            boletos_vendidos=boletos_vendidos+1
            self.D3.setChecked(True)
            self.D3.setDisabled(True)
        if(disabled_D4==True):
            boletos_vendidos=boletos_vendidos+1
            self.D4.setChecked(True)
            self.D4.setDisabled(True)
        if(disabled_D5==True):
            boletos_vendidos=boletos_vendidos+1
            self.D5.setChecked(True)
            self.D5.setDisabled(True)
        if(disabled_E1==True):
            boletos_vendidos=boletos_vendidos+1
            self.E1.setChecked(True)
            self.E1.setDisabled(True)
        if(disabled_E2==True):
            boletos_vendidos=boletos_vendidos+1
            self.E2.setChecked(True)
            self.E2.setDisabled(True)
        if(disabled_E3==True):
            boletos_vendidos=boletos_vendidos+1
            self.E3.setChecked(True)
            self.E3.setDisabled(True)
        if(disabled_E4==True):
            boletos_vendidos=boletos_vendidos+1
            self.E4.setChecked(True)
            self.E4.setDisabled(True)
        if(disabled_E5==True):
            boletos_vendidos=boletos_vendidos+1
            self.E5.setChecked(True)
            self.E5.setDisabled(True)
        
        ### CARGAR VENTAS AL REABRIR EL MENU ###
        self.actualizarVentas()
        
        ### BOTON VOLVER Y COMPRAR ###
        self.BotonVolver.clicked.connect(P2Funcion2.close) #Boton para cerrar la ventana
        self.BotonComprar.clicked.connect(self.onActionComprar) #Boton para comprar, revisa si las checkbox estan activas y ejecuta la compra
        
    ### AL PRESIONAR EL BOTON COMPRAR VENDER EL BOLETO Y DESACTIVAR EL CHECKBOX, ADEMÁS DE ACTUALIZAR LA INFORMACIÓN DE VENTA ###
    def onActionComprar(self):
        global boletos_vendidos
        global disabled_A1, disabled_A2, disabled_A3, disabled_A4, disabled_A5, disabled_B1, disabled_B2, disabled_B3, disabled_B4, disabled_B5, disabled_C1, disabled_C2, disabled_C3, disabled_C4, disabled_C5, disabled_D1, disabled_D2, disabled_D3, disabled_D4, disabled_D5, disabled_E1, disabled_E2, disabled_E3, disabled_E4, disabled_E5
        ### PARA QUE NO SE AUMENTE EL VALOR AL COMPRAR UN TICKET YA MARCADO Y DESHABILITADO ###
        if(self.A1.isChecked()==True or self.A2.isChecked()==True or self.A3.isChecked()==True or self.A4.isChecked()==True or self.A5.isChecked()==True or 
           self.B1.isChecked()==True or self.B2.isChecked()==True or self.B3.isChecked()==True or self.B4.isChecked()==True or self.B5.isChecked()==True or 
           self.C1.isChecked()==True or self.C2.isChecked()==True or self.C3.isChecked()==True or self.C4.isChecked()==True or self.C5.isChecked()==True or 
           self.D1.isChecked()==True or self.D2.isChecked()==True or self.D3.isChecked()==True or self.D4.isChecked()==True or self.D5.isChecked()==True or 
           self.E1.isChecked()==True or self.E2.isChecked()==True or self.E3.isChecked()==True or self.E4.isChecked()==True or self.E5.isChecked()==True):
            boletos_vendidos=0
        if(self.A1.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.A1.setDisabled(True)
            disabled_A1=True
        if(self.A2.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.A2.setDisabled(True)
            disabled_A2=True
        if(self.A3.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.A3.setDisabled(True)
            disabled_A3=True
        if(self.A4.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.A4.setDisabled(True)
            disabled_A4=True
        if(self.A5.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.A5.setDisabled(True)
            disabled_A5=True
        if(self.B1.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.B1.setDisabled(True)
            disabled_B1=True
        if(self.B2.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.B2.setDisabled(True)
            disabled_B2=True
        if(self.B3.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.B3.setDisabled(True)
            disabled_B3=True
        if(self.B4.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.B4.setDisabled(True)
            disabled_B4=True
        if(self.B5.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.B5.setDisabled(True)
            disabled_B5=True
        if(self.C1.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.C1.setDisabled(True)
            disabled_C1=True
        if(self.C2.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.C2.setDisabled(True)
            disabled_C2=True
        if(self.C3.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.C3.setDisabled(True)
            disabled_C3=True
        if(self.C4.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.C4.setDisabled(True)
            disabled_C4=True
        if(self.C5.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.C5.setDisabled(True)
            disabled_C5=True
        if(self.D1.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.D1.setDisabled(True)
            disabled_D1=True
        if(self.D2.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.D2.setDisabled(True)
            disabled_D2=True
        if(self.D3.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.D3.setDisabled(True)
            disabled_D3=True
        if(self.D4.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.D4.setDisabled(True)
            disabled_D4=True
        if(self.D5.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.D5.setDisabled(True)
            disabled_D5=True
        if(self.E1.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.E1.setDisabled(True)
            disabled_E1=True
        if(self.E2.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.E2.setDisabled(True)
            disabled_E2=True
        if(self.E3.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.E3.setDisabled(True)
            disabled_E3=True
        if(self.E4.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.E4.setDisabled(True)
            disabled_E4=True
        if(self.E5.isChecked()==True):
            boletos_vendidos=boletos_vendidos+1
            self.E5.setDisabled(True)
            disabled_E5=True
            
        self.actualizarVentas()
        
    ### ACTUALIZAR INFORMACIÓN DE LAS VENTAS ###
    def actualizarVentas(self):
        global ventasTotalesP2F2
        ventasTotalesP2F2=boletos_vendidos*3000
        self.TextoEditable_TOTAL.setText("$" + str(boletos_vendidos*3000))
        self.TextoEditable_BoletosVendidos.setText(str(boletos_vendidos))
        self.TextoEditable_AsientosDisponibles.setText(str(25-boletos_vendidos))
        self.TextoEditable_AsientosOcupados.setText(str(boletos_vendidos))
        
    ### FIN CONTROLADOR ###
        
    ### DEFINIR TEXTOS A-E, 1-5, BOTONES ENTRE OTROS ###
    def definirTextos(self, P2Funcion2):
        P2Funcion2.setWindowTitle("Cars - Funcion 2 - Cinema PM")
        self.TextoA.setText("A")
        self.TextoB.setText("B")
        self.TextoC.setText("C")
        self.TextoD.setText("D")
        self.TextoE.setText("E")
        self.Texto1.setText("1")
        self.Texto2.setText("2")
        self.Texto3.setText("3")
        self.Texto4.setText("4")
        self.Texto5.setText("5")
        self.TextoAsientoDisponibles.setText("Asiento\nDisponibles")
        self.TextoAsientosOcupados.setText("Asientos\nOcupados")
        self.TextoBoletosVendidos.setText("Boletos\nVendidos")
        self.TextoTOTAL.setText("TOTAL")
        self.BotonVolver.setText("Volver")
        self.BotonComprar.setText("Comprar")

        ### DESHABILITAR QUE SE PUEDA EDITAR EL TEXTO ###
        self.TextoEditable_AsientosDisponibles.setEnabled(False)
        self.TextoEditable_AsientosOcupados.setEnabled(False)
        self.TextoEditable_BoletosVendidos.setEnabled(False)
        self.TextoEditable_TOTAL.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    P2Funcion2 = QtWidgets.QMainWindow()
    ui = Ui_P2Funcion2()
    ui.setupUi(P2Funcion2)
    P2Funcion2.show()
    sys.exit(app.exec_())
