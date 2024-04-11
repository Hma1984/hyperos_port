import shutil
from echo import red
import sys


def main():
    for i in ['unzip', 'aria2c', '7z', 'zip', 'java', 'zipalign', 'python3', 'zstd']:
        if not shutil.which(i):
            red(f"--> Missing {i} abort! please run ./setup.sh first (sudo is required on Linux system)")
            red(f"--> 命令 {i} 缺失!请重新运行setup.sh (Linux系统sudo ./setup.sh)")
            sys.exit(1)


if __name__ == '__main__':
    main()