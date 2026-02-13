#!/bin/bash

# 检查7z是否在PATH中
if ! command -v 7z &> /dev/null; then
    echo "Error: 7z is not in PATH"
    exit 1
fi

# 使用pyinstaller打包项目到release目录
pyinstaller --distpath ./release pyinstaller.spec

# 复制j2template到release目录
cp -r j2template ./release

# 将release目录内容打包成以svd2header为根目录的zip压缩包
7z a -tzip svd2header.zip ./release/* -r

# 将压缩包移动到release目录
mv svd2header.zip ./release/
