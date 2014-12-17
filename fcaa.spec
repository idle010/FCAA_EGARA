# -*- mode: python -*-
a = Analysis(['fcaa.py'],
             pathex=['/home/lsdir/FCAA_EGARA'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='fcaa',
          debug=False,
          strip=None,
          upx=True,
          console=True )
