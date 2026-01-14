#!/usr/bin/env python3
"""
qrcode49 - 二维码生成与解析命令行工具

根据输入文件类型自动切换功能：
- 输入文本文件(.txt, .md) → 生成二维码图片
- 输入图片文件(.png, .jpg, .webp) → 解析二维码内容
"""

import argparse
import os
import sys
from pathlib import Path

import cv2
import qrcode

# 支持的文件扩展名
TEXT_EXTENSIONS: set[str] = {'.txt', '.md'}
IMAGE_EXTENSIONS: set[str] = {'.png', '.jpg', '.jpeg', '.webp'}


def is_text_file(file_path: str) -> bool:
    """判断是否为文本文件"""
    return Path(file_path).suffix.lower() in TEXT_EXTENSIONS


def is_image_file(file_path: str) -> bool:
    """判断是否为图片文件"""
    return Path(file_path).suffix.lower() in IMAGE_EXTENSIONS


def generate_qrcode(text: str, output_path: str, box_size: int = 10) -> None:
    """
    生成二维码图片

    Args:
        text: 要编码的文本内容
        output_path: 输出图片路径
        box_size: 二维码每个模块的像素大小（边长参数）
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # JPEG 格式需要转换为 RGB 模式
    output_ext = Path(output_path).suffix.lower()
    if output_ext in {'.jpg', '.jpeg'}:
        img = img.convert('RGB')

    img.save(output_path)
    print(f"✅ 二维码已生成：{output_path}")


def decode_qrcode(image_path: str, output_path: str) -> None:
    """
    解析图片中的二维码

    Args:
        image_path: 输入图片路径
        output_path: 输出文本文件路径
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"无法读取图片文件：{image_path}")

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if not data:
        raise ValueError("未在图片中检测到二维码")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(data)

    print(f"✅ 二维码内容已解析并保存到：{output_path}")
    print(f"📝 解析内容：{data}")


def validate_input_file(file_path: str) -> None:
    """验证输入文件是否存在"""
    if not os.path.exists(file_path):
        print(f"❌ 错误：输入文件不存在：{file_path}")
        sys.exit(1)


def validate_box_size(box_size: int) -> None:
    """验证边长参数"""
    if box_size < 1:
        print(f"❌ 错误：边长必须大于 0")
        sys.exit(1)


def validate_output_format(input_file: str, output_file: str) -> None:
    """验证输出文件格式是否匹配输入类型"""
    if is_text_file(input_file) and not is_image_file(output_file):
        print(f"❌ 错误：输出文件必须是图片格式（.png, .jpg, .webp）")
        sys.exit(1)

    if is_image_file(input_file) and not is_text_file(output_file):
        print(f"❌ 错误：输出文件必须是文本格式（.txt, .md）")
        sys.exit(1)


def handle_text_to_image(input_file: str, output_file: str, box_size: int) -> None:
    """处理文本文件生成二维码"""
    print(f"📄 检测到文本文件，开始生成二维码...")

    with open(input_file, 'r', encoding='utf-8') as f:
        text_content = f.read()

    if not text_content:
        print(f"❌ 错误：输入文本文件为空")
        sys.exit(1)

    generate_qrcode(text_content, output_file, box_size)


def handle_image_to_text(input_file: str, output_file: str) -> None:
    """处理图片文件解析二维码"""
    print(f"🖼️  检测到图片文件，开始解析二维码...")
    decode_qrcode(input_file, output_file)


def main() -> None:
    """主函数：解析命令行参数并执行对应操作"""
    parser = argparse.ArgumentParser(
        description='qrcode49 - 二维码生成与解析工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例：
  生成二维码：qrcode49 input.txt output.png [边长]
  解析二维码：qrcode49 input.png output.txt

注意：
  - 边长参数可选，默认为 10
  - 边长越大，二维码图片越大
        """
    )

    parser.add_argument('input_file', help='输入文件路径（文本文件或图片文件）')
    parser.add_argument('output_file', help='输出文件路径')
    parser.add_argument('box_size', nargs='?', type=int, default=10,
                        help='二维码边长（每个模块的像素大小），默认 10')

    args = parser.parse_args()

    validate_input_file(args.input_file)
    validate_box_size(args.box_size)
    validate_output_format(args.input_file, args.output_file)

    try:
        if is_text_file(args.input_file):
            handle_text_to_image(args.input_file, args.output_file, args.box_size)
        elif is_image_file(args.input_file):
            handle_image_to_text(args.input_file, args.output_file)
        else:
            print(f"❌ 错误：不支持的文件类型：{args.input_file}")
            print(f"   支持的输入格式：.txt, .md, .png, .jpg, .webp")
            sys.exit(1)

    except Exception as e:
        print(f"❌ 执行失败：{e}")
        sys.exit(1)


if __name__ == '__main__':
    main()