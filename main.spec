# -*- mode: python ; coding: utf-8 -*-

import sys
import os
from pathlib import Path

# 1. Configurazione base
BASE_DIR = Path.cwd()
APP_NAME = "GestioneMagazzino"

# 2. File e cartelle da includere
data_files = [
    (os.path.join(BASE_DIR, 'database', 'magazzino.db'), 'database'),
    (os.path.join(BASE_DIR, 'gui'), 'gui'),
    (os.path.join(BASE_DIR, 'models'), 'models'),
    (os.path.join(BASE_DIR, 'utils'), 'utils'),
    # Aggiungi altre risorse se necessario:
    # (os.path.join(BASE_DIR, 'resources', '*'), 'resources')
]

# 3. Configurazione Analysis
a = Analysis(
    ['main.py'],
    pathex=[str(BASE_DIR)],
    binaries=[],
    datas=data_files,
    hiddenimports=[
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'sqlite3'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'unittest', 'pydoc'],
    noarchive=False,
    optimize=1
)

# 4. Configurazione PYZ
pyz = PYZ(a.pure, a.zipped_data)

# 5. Configurazione EXE (base)
exe = EXE(
    pyz,
    a.scripts,
    name=APP_NAME,
    debug=False,
    strip=False,
    upx=True,
    console=False  # Imposta True per debug
)

# 6. Configurazione COLLECT per OneDir
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name=APP_NAME
)