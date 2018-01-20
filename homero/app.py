# -*- coding: utf-8 -*-
import os
import fnmatch
import sys

package = 'uncompyle6'

try:
    __import__('%s' % package)
except:
    # Validar sistema operativo actual para instalar la librería, usando el comando correcto.
    from sys import platform

    comando = os.system('gksudo pip install %s' % package) \
        if platform == 'linux' or platform == 'linux2' else os.system('pip install %s' % package)


class App(object):
    def __init__(self):
        pass

    def buscar_archivos(self, patrones, ruta):
        """
            Método que ``busca`` los archivos `.pyc` en la ruta que se le asigna.
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        :param patrones: Una lista con el patrón o patrones a descompilar
        :param ruta: Una cadena con la ruta en donde se buscarán los archivos.
        :return: Una lista con la ruta o las rutas encontradas con archivos.
        """
        resultado = []
        for raiz, dirs, archivos in os.walk(ruta):
            for name in archivos:
                if isinstance(patrones, list):
                    for patron in patrones:
                        if fnmatch.fnmatch(name, patron):
                            resultado.append(os.path.join(raiz, name))
                else:
                    raise TypeError("Debes agregar una lista como primer parámetro, en lugar de %s" % type(patrones))
        return resultado

    def descompilar(self, rutalocal=None, ruta_busqueda=None, descompilar=False, descompilar_init=False):
        """
            Método que ``descompila`` los archivos `.pyc` a `.py`
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        :param rutalocal: Una cadena con la ruta en donde se guardarán los archivos descompilados.
        :param ruta_busqueda: Una cadena con la ruta de busqueda de los archivos.
        :param descompilar: Un boleano para los tests, no descompila en `False`
        :param descompilar_init: Un boleano para descompilar los archivos `__init__.pyc`
        :return: Los archivos descompilados o un error si hubo un problema.
        """
        # file_init = None
        # TODO: restructurar esta sección para evitar sobreescribir archivos
        comando = None
        uncompile_all = True
        init_file = None
        if descompilar_init:
            init_file = '*__init__.pyc'
        archivos = self.buscar_archivos(['*.pyc'], ruta_busqueda if ruta_busqueda is not None else '/home')
        for archivo in archivos:
            if descompilar_init:
                if '__init__.pyc' in archivo:
                    pass
            print("# All pyc archivos", archivo)
            comando = '%s' % archivo
        if descompilar:
            # TODO: Verificar si el commando funciona con windows.
            os.system('uncompyle6 -o %s %s' % (rutalocal, comando))


app = App()


if __name__ == '__main__':
    app.descompilar('/home/eortiz/prueba/', '/home/eortiz/odoo_addons', descompilar=False, descompilar_init=True)