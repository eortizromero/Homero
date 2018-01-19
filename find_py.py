# -*- coding: utf-8 -*-
import os
import fnmatch
import sys

package = 'uncompyle6'

try:
    __import__('%s' % package)
except:
    # TODO: valid current os for custom command
    from sys import platform

    command = os.system('gksudo pip install %s' % package) \
        if platform == 'linux' or platform == 'linux2' else os.system('pip install %s' % package)


def find(patterns, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if isinstance(patterns, list):
                for pattern in patterns:
                    if fnmatch.fnmatch(name, pattern):
                        result.append(os.path.join(root, name))
            else:
                raise TypeError("You need a list as the first argument, instead of %s" % type(patterns))
    return result


def descompilar(local_path=None, from_uncompile_path=None, desc=False, uncompile_init=False):
    # file_init = None
    # TODO: restructurar esta sección para evitar sobreescribir archivos
    command = None
    uncompile_all = True
    init_file = None
    if uncompile_init:
        init_file = '*__init__.pyc'
        # init = find(['*__init__.pyc'], from_uncompile_path)
        # for f in init:
        #     print("# Init files ", f)
        #     command = '%s' % f
    files = find(['*.pyc'], from_uncompile_path if from_uncompile_path is not None else '/home')
    for file in files:
        if uncompile_init:
            if '__init__.pyc' in file:
                pass
        print("# All pyc files", file)
        command = '%s' % file
    if desc:
        os.system('uncompyle6 -o %s %s' % (local_path, command))


if __name__ == '__main__':
    descompilar('/home/eortiz/prueba/', '/home/eortiz/odoo_addons', desc=False, uncompile_init=True)