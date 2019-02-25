# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('main.py', targetName='Dungeon world', base='Win32GUI')]

excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib',
            'xml', 'bz2']

zip_include_packages = ['collections', 'encodings', 'importlib']

include_files = ['data', 'permanent', 'Levels', 'HP', 'goblin', 'fire_magician', 'fire_ball']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
        'include_files': include_files,
    }
}

setup(name='dungeon world',
      version='0.0.1',
      description='Мы что-то сделали',
      executables=executables,
      options=options)