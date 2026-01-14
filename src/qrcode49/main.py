#!/usr/bin/env python3
"""
qrcode49 - 二维码生成与解析工具

根据输入文件类型，自动在"生成二维码"和"解析二维码"之间切换。
"""

import sys
import os
from pathlib import Path

import qrcode
import qrcode.image.svg
import cv2


def is_text_file(filepath: str) -> bool:
    """判断文件是否为文本文件（.txt 或 .md）"""
    text_extensions = {'.txt', '.md'}
    return Path(filepath).suffix.lower() in text_extensions


def is_image_file(filepath: str) -> bool:
    """判断文件是否为图片文件（.png, .jpg, .webp, .svg）"""
    image_extensions = {'.png', '.jpg', '.jpeg', '.webp', '.svg'}
    return Path(filepath).suffix.lower() in image_extensions


def generate_qrcode(text_file: str, output_file: str) -> None:
    """
    生成二维码：从文本文件读取内容，生成二维码图片

    Args:
        text_file: 输入文本文件路径
        output_file: 输出图片文件路径
    """
    # 读取文本文件内容
    try:
        with open(text_file, 'r', encoding='utf-8') as f:
            text_content = f.read()
    except FileNotFoundError:
        print(f"错误：找不到文件 '{text_file}'")
        sys.exit(1)
    except Exception as e:
        print(f"错误：读取文件失败 - {e}")
        sys.exit(1)

    # 检查文本内容是否为空
    if not text_content.strip():
        print("错误：文本文件内容为空")
        sys.exit(1)

    # 根据输出文件扩展名选择生成方式
    output_ext = Path(output_file).suffix.lower()

    try:
        # 二维码通用配置
        qr_config = {
            'version': 1,
            'error_correction': qrcode.constants.ERROR_CORRECT_L,
            'box_size': 10,
            'border': 4,
        }

        if output_ext == '.svg':
            # 生成 SVG 矢量图
            qr = qrcode.QRCode(
                image_factory=qrcode.image.svg.SvgPathImage,
                **qr_config
            )
            qr.add_data(text_content)
            qr.make(fit=True)
            img = qr.make_image()

            # 保存 SVG 文件
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(img.to_string(encoding='unicode'))
        else:
            # 生成位图（PNG, JPG, WEBP）
            qr = qrcode.QRCode(**qr_config)
            qr.add_data(text_content)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # 保存图片文件
            img.save(output_file)

        print(f"✓ 二维码已成功生成：{output_file}")
    except Exception as e:
        print(f"错误：生成二维码失败 - {e}")
        sys.exit(1)


def decode_qrcode(image_file: str, output_file: str) -> None:
    """
    解析二维码：从图片文件读取二维码内容，写入到文本文件

    Args:
        image_file: 输入图片文件路径
        output_file: 输出文本文件路径
    """
    # 读取图片文件
    img = cv2.imread(image_file)
    if img is None:
        print(f"错误：无法读取图片文件 '{image_file}'")
        sys.exit(1)

    # 使用 OpenCV 的二维码检测器
    detector = cv2.QRCodeDetector()

    # 检测并解码二维码
    try:
        data, bbox, _ = detector.detectAndDecode(img)

        if not data:
            print("错误：未在图片中检测到二维码")
            sys.exit(1)

        # 将解码结果写入文本文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f"✓ 二维码解析成功，内容已写入：{output_file}")
    except Exception as e:
        print(f"错误：解析二维码失败 - {e}")
        sys.exit(1)


def main():
    """主函数：处理命令行参数并执行相应操作"""
    # 检查命令行参数数量
    if len(sys.argv) != 3:
        print("使用方法：qrcode49 <输入文件> <输出文件>")
        print("\n功能说明：")
        print("  - 如果输入文件是文本文件（.txt, .md）：生成二维码图片")
        print("  - 如果输入文件是图片文件（.png, .jpg, .webp）：解析二维码内容")
        print("\n示例：")
        print("  qrcode49 input.txt output.png    # 生成二维码")
        print("  qrcode49 input.png output.txt    # 解析二维码")
        print("\n注意：SVG 格式仅支持生成，不支持解析")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：输入文件 '{input_file}' 不存在")
        sys.exit(1)

    # 根据输入文件类型执行相应操作
    if is_text_file(input_file):
        print(f"检测到文本文件，正在生成二维码...")
        generate_qrcode(input_file, output_file)
    elif is_image_file(input_file):
        print(f"检测到图片文件，正在解析二维码...")
        decode_qrcode(input_file, output_file)
    else:
        print(f"错误：不支持的文件类型 '{Path(input_file).suffix}'")
        print("支持的输入格式：.txt, .md, .png, .jpg, .jpeg, .webp")
        print("注意：SVG 格式仅支持生成，不支持解析")
        sys.exit(1)


if __name__ == "__main__":
    main()