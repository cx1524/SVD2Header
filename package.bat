@echo off

REM 检查7z是否在PATH中
7z.exe >nul 2>&1
if errorlevel 1 (
    echo Error: 7z is not in PATH
    exit /b 1
)

REM 使用pyinstaller打包项目到release目录
pyinstaller --distpath ./release pyinstaller.spec

REM 复制j2template到release目录
xcopy j2template release\j2template /s /i /y

REM 将release目录内容打包成以svd2header为根目录的zip压缩包
7z.exe a -tzip svd2header.zip release\* -r

REM 将压缩包移动到release目录
move svd2header.zip release\
