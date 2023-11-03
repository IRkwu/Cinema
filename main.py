import sys

from view.MenuPrincipal import Ui_VentanaPrincipal

from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget


class VentanaPrincipal(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)
                
        self.show()          

if __name__ == "__main__":
    print("Iniciando Cinema PM")
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    sys.exit(app.exec_())