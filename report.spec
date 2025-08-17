# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['report.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('images', 'images'), 
        ('rms.db', '.'),
        ('course.py', '.'),
        ('student.py', '.'),
        ('result.py', '.'),
        ('dashboard.py', '.')
    ],
    hiddenimports=[
        'PIL._tkinter_finder',
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'sqlite3',
        'reportlab',
        'reportlab.lib.pagesizes',
        'reportlab.pdfgen'
    ],
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
    name='report',
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
