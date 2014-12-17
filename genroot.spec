# -*- mode: python -*-
a = Analysis(['genroot.py'],
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
          name='genroot',
          debug=False,
          strip=None,
          upx=True,
          console=True )
