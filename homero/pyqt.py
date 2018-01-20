# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QApplication
import sys


class Meta(type):
    """
        Clase Meta para aplicar el decorador automáticamente a todas las funciones
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    def __new__(meta, nombre, bases, atributos):
        for clave, valor in list(atributos.items()):
            print(clave, valor)
        return type.__new__(meta, nombre, bases, atributos)


class Base(object):
    __metaclass__ = Meta


BaseAbstracta = Base


class MainWindow(QMainWindow, BaseAbstracta):
    def __init__(self):
        """
            En esta clase no se dibujará la interfáz manual, la crearemos con el `diseñador` de PyQt.
            Se carga mediante el archivo `main_window.ui`, o el archivo `main_window.py`.
        """
        super(MainWindow, self).__init__()
        self.setWindowTitle("Descompilador")
        self.resize(300, 400)

    def cargar_accion(self, accion, funcion=None, **opciones):
        print(accion, funcion, opciones)
        tipo = opciones.pop('tipo', None)
        if tipo is None:
            tipo = 'boton'
            pass  # Tipo predeterminado será boton

    def accion(self, accion, **opciones):
        """
            Decorador que maneja las acciones de cada elemeto
        :param accion: Una cadena con la accion que ejecutará el boton.
        :param opciones: Un diccionario de opciones adicionales con el tipo de elemento que ejecutará esa acción.
        :return: la función decorador, llamando al :meth `cargar_accion`:.
        """
        def decorador(funcion):
            self.cargar_accion(accion, funcion, **opciones)
            return funcion
        return decorador

    @accion('agregar', tipo='boton')
    def buscar_ruta(self):
        pass


main_window = MainWindow

aplicacion = QApplication(sys.argv)


def iniciar(ventana):
    v = ventana
    v.show()
    sys.exit(aplicacion.exec_())


