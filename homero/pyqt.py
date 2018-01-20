# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QApplication
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Descompilador")
        self.resize(300, 400)

    def cargar_accion(self, accion, funcion=None, **opciones):
        print(accion, funcion, opciones)

    def accion(self, accion, **opciones):
        def decorador(funcion):
            self.cargar_accion(accion, funcion, **opciones)
            return funcion
        return decorador


main_window = MainWindow

aplicacion = QApplication(sys.argv)


def iniciar(ventana):
    v = ventana
    v.show()
    sys.exit(aplicacion.exec_())


