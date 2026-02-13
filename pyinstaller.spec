# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],                      # 主入口脚本，按需修改
    pathex=[],                        # 额外模块搜索路径
    binaries=[],                      # 需打包的外部二进制文件
    datas=[],                         # 需打包的额外资源（文件夹、配置文件等）
    hiddenimports=[
        'parser',
        'jinja2'
        ],                 # 隐式导入的模块
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],                      # 排除的模块
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='svd2header',             # 生成的可执行文件名称
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,                     # 如需窗口程序，改为 False
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='',             # 图标文件（可选）
)
