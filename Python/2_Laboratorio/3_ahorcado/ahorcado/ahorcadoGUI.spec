# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\rodri\\OneDrive\\Desktop\\US_VSCode\\VSCode FP\\Python\\laboratorio\\clase2_(3-10)\\ahorcado\\ahorcadoGUI.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\rodri\\OneDrive\\Desktop\\US_VSCode\\VSCode FP\\Python\\laboratorio\\clase2_(3-10)\\data\\palabras_ahorcado.txt', 'data')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ahorcadoGUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
