#!/usr/bin/env python3
"""qrcode49 - 简洁友好的二维码工具

支持两种模式：
1. 交互式向导模式: uv run qrcode49
2. 命令行模式: uv run qrcode49 input.txt output.png
"""

import sys
from pathlib import Path
from qrcode49.core import generate_qrcode, decode_qrcode
from qrcode49.config import TEXT_EXTENSIONS, IMAGE_EXTENSIONS, DEFAULT_BOX_SIZE


def is_text_file(path: str) -> bool:
    """判断是否为文本文件"""
    return Path(path).suffix.lower() in TEXT_EXTENSIONS


def is_image_file(path: str) -> bool:
    """判断是否为图片文件"""
    return Path(path).suffix.lower() in IMAGE_EXTENSIONS


def print_success(msg: str) -> None:
    """打印成功消息"""
    print(f"✅ {msg}")


def print_error(msg: str) -> None:
    """打印错误消息"""
    print(f"❌ {msg}", file=sys.stderr)


def print_info(msg: str) -> None:
    """打印信息消息"""
    print(f"ℹ️  {msg}")


def interactive_mode() -> int:
    """交互式向导模式

    Returns:
        退出码
    """
    print("\n🎯 二维码工具 - 交互式向导\n")

    # 选择操作类型
    print("请选择操作:")
    print("  1. 生成二维码（文本 → 图片）")
    print("  2. 解析二维码（图片 → 文本）")

    choice = input("\n请输入选项 (1 或 2): ").strip()

    if choice == "1":
        return interactive_generate()
    elif choice == "2":
        return interactive_decode()
    else:
        print_error("无效的选项")
        return 1


def interactive_generate() -> int:
    """交互式生成二维码

    Returns:
        退出码
    """
    print("\n📝 生成二维码模式\n")

    # 输入文件路径
    input_path = input("输入文本文件路径: ").strip()
    if not input_path:
        print_error("请输入文件路径")
        return 1

    if not Path(input_path).exists():
        print_error(f"文件不存在: {input_path}")
        return 1

    if not is_text_file(input_path):
        print_error(f"不支持的文件类型，请使用: {', '.join(TEXT_EXTENSIONS)}")
        return 1

    # 输出文件路径
    default_output = Path(input_path).stem + ".png"
    output_path = input(f"输出图片路径 (默认: {default_output}): ").strip()
    if not output_path:
        output_path = default_output

    # 边长参数
    box_size_input = input(f"二维码边长 (默认: {DEFAULT_BOX_SIZE}): ").strip()
    box_size = int(box_size_input) if box_size_input else DEFAULT_BOX_SIZE

    # 确认
    print(f"\n操作确认:")
    print(f"  输入: {input_path}")
    print(f"  输出: {output_path}")
    print(f"  边长: {box_size}")

    confirm = input("\n确认执行? (y/n): ").strip().lower()
    if confirm != "y":
        print_info("已取消")
        return 0

    # 执行生成
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()

        generate_qrcode(text, output_path, box_size=box_size)
        print_success(f"二维码已生成: {output_path}")
        return 0

    except Exception as e:
        print_error(str(e))
        return 1


def interactive_decode() -> int:
    """交互式解析二维码

    Returns:
        退出码
    """
    print("\n🔍 解析二维码模式\n")

    # 输入文件路径
    input_path = input("输入图片文件路径: ").strip()
    if not input_path:
        print_error("请输入文件路径")
        return 1

    if not Path(input_path).exists():
        print_error(f"文件不存在: {input_path}")
        return 1

    if not is_image_file(input_path):
        print_error(f"不支持的文件类型，请使用: {', '.join(IMAGE_EXTENSIONS)}")
        return 1

    # 输出文件路径
    default_output = Path(input_path).stem + ".txt"
    output_path = input(f"输出文本路径 (默认: {default_output}): ").strip()
    if not output_path:
        output_path = default_output

    # 确认
    print(f"\n操作确认:")
    print(f"  输入: {input_path}")
    print(f"  输出: {output_path}")

    confirm = input("\n确认执行? (y/n): ").strip().lower()
    if confirm != "y":
        print_info("已取消")
        return 0

    # 执行解析
    try:
        content = decode_qrcode(input_path)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print_success(f"二维码内容已保存: {output_path}")
        print_info(f"内容: {content[:50]}{'...' if len(content) > 50 else ''}")
        return 0

    except Exception as e:
        print_error(str(e))
        return 1


def command_line_mode(args: list[str]) -> int:
    """命令行模式

    Args:
        args: 命令行参数列表

    Returns:
        退出码
    """
    if len(args) < 2:
        print_error("用法: qrcode49 <输入文件> <输出文件> [边长]")
        print_info("示例:")
        print_info("  生成: qrcode49 input.txt output.png")
        print_info("  解析: qrcode49 input.png output.txt")
        return 1

    input_file = args[0]
    output_file = args[1]
    box_size = int(args[2]) if len(args) > 2 else DEFAULT_BOX_SIZE

    # 验证输入文件
    if not Path(input_file).exists():
        print_error(f"输入文件不存在: {input_file}")
        return 1

    # 根据输入文件类型执行操作
    if is_text_file(input_file):
        print_info("检测到文本文件，生成二维码...")
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                text = f.read()

            generate_qrcode(text, output_file, box_size=box_size)
            print_success(f"二维码已生成: {output_file}")
            return 0

        except Exception as e:
            print_error(str(e))
            return 1

    elif is_image_file(input_file):
        print_info("检测到图片文件，解析二维码...")
        try:
            content = decode_qrcode(input_file)

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(content)

            print_success(f"二维码内容已保存: {output_file}")
            print_info(f"内容: {content[:50]}{'...' if len(content) > 50 else ''}")
            return 0

        except Exception as e:
            print_error(str(e))
            return 1

    else:
        print_error(f"不支持的文件类型: {Path(input_file).suffix}")
        print_info(f"支持的格式: {', '.join(TEXT_EXTENSIONS | IMAGE_EXTENSIONS)}")
        return 1


def main() -> int:
    """主函数

    Returns:
        退出码
    """
    try:
        # 检查是否有参数
        if len(sys.argv) > 1:
            # 命令行模式
            return command_line_mode(sys.argv[1:])
        else:
            # 交互式向导模式
            return interactive_mode()

    except KeyboardInterrupt:
        print_info("\n操作已取消")
        return 130
    except Exception as e:
        print_error(f"发生错误: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
