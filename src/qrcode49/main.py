#!/usr/bin/env python3
"""
qrcode49 - 二维码生成与解析命令行工具

根据输入文件类型自动切换功能：
- 输入文本文件(.txt, .md) → 生成二维码图片
- 输入图片文件(.png, .jpg, .webp) → 解析二维码内容

这是程序的入口文件，所有核心逻辑都在其他模块中实现。
"""

import sys

from qrcode49.cli import run_cli


def main() -> None:
    """
    主函数：运行命令行接口

    该函数是程序的入口点，负责调用 CLI 模块处理用户命令。
    所有业务逻辑都在 cli.py 模块中实现。
    """
    # 运行命令行接口，并获取退出码
    exit_code = run_cli()

    # 使用退出码退出程序
    sys.exit(exit_code)


if __name__ == '__main__':
    main()