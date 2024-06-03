# 打包成exe的方法
要将Python脚本打包成可执行文件（.exe），可以使用PyInstaller。这是一个常用的工具，可以将Python脚本打包成独立的可执行文件。
## Step 1: 安装 PyInstaller
pip install pyinstaller

## Step 2: 导航到脚本所在目录
cd path/to/your/script

## Step 3: 打包脚本
pyinstaller --onefile con_click.py