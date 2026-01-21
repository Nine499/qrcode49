"""
命令行接口模块

该模块提供命令行接口，处理用户输入和输出。
"""

import argparse
import sys

from qrcode49.config import DEFAULT_BOX_SIZE
from qrcode49.decoder import QRCodeDecoder
from qrcode49.exceptions import QRCodeError
from qrcode49.generator import QRCodeGenerator
from qrcode49.validators import (
    validate_box_size,
    validate_file_exists,
    validate_file_readable,
    validate_file_type_supported,
    validate_is_file,
    validate_output_format,
    is_image_file,
    is_text_file,
)


def create_parser() -> argparse.ArgumentParser:
    """
    创建命令行参数解析器

    Returns:
        配置好的 ArgumentParser 对象
    """
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
  - 文本文件格式：.txt, .md
  - 图片文件格式：.png, .jpg, .jpeg, .webp
        """
    )

    parser.add_argument(
        'input_file',
        help='输入文件路径（文本文件或图片文件）'
    )
    parser.add_argument(
        'output_file',
        help='输出文件路径'
    )
    parser.add_argument(
        'box_size',
        nargs='?',
        type=int,
        default=DEFAULT_BOX_SIZE,
        help=f'二维码边长（每个模块的像素大小），默认 {DEFAULT_BOX_SIZE}'
    )

    return parser


def handle_text_to_image(input_file: str, output_file: str, box_size: int) -> None:
    """
    处理文本文件生成二维码

    Args:
        input_file: 输入文本文件路径
        output_file: 输出图片文件路径
        box_size: 二维码边长参数

    Raises:
        QRCodeError: 如果处理失败
    """
    print(f"📄 检测到文本文件，开始生成二维码...")

    # 创建生成器并生成二维码
    generator = QRCodeGenerator(box_size=box_size)
    generator.generate_from_file(input_file, output_file)

    print(f"✅ 二维码已生成：{output_file}")


def handle_image_to_text(input_file: str, output_file: str) -> None:
    """
    处理图片文件解析二维码

    Args:
        input_file: 输入图片文件路径
        output_file: 输出文本文件路径

    Raises:
        QRCodeError: 如果处理失败
    """
    print(f"🖼️  检测到图片文件，开始解析二维码...")

    # 创建解析器并解析二维码
    decoder = QRCodeDecoder()
    content = decoder.decode(input_file)

    # 保存解析结果
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 二维码内容已解析并保存到：{output_file}")
    print(f"📝 解析内容：{content}")


def validate_inputs(input_file: str, output_file: str, box_size: int) -> None:
    """
    验证所有输入参数

    Args:
        input_file: 输入文件路径
        output_file: 输出文件路径
        box_size: 二维码边长参数

    Raises:
        QRCodeError: 如果验证失败
    """
    # 验证输入文件
    validate_file_exists(input_file)
    validate_is_file(input_file)
    validate_file_readable(input_file)
    validate_file_type_supported(input_file)

    # 验证边长参数
    validate_box_size(box_size)

    # 验证输出格式
    validate_output_format(input_file, output_file)


def run_cli(args: list[str] | None = None) -> int:
    """
    运行命令行接口

    Args:
        args: 命令行参数列表，如果为 None 则使用 sys.argv

    Returns:
        退出码，0 表示成功，非 0 表示失败
    """
    try:
        # 解析命令行参数
        parser = create_parser()
        parsed_args = parser.parse_args(args)

        # 验证输入参数
        validate_inputs(
            parsed_args.input_file,
            parsed_args.output_file,
            parsed_args.box_size
        )

        # 根据输入文件类型执行相应操作
        if is_text_file(parsed_args.input_file):
            handle_text_to_image(
                parsed_args.input_file,
                parsed_args.output_file,
                parsed_args.box_size
            )
        elif is_image_file(parsed_args.input_file):
            handle_image_to_text(
                parsed_args.input_file,
                parsed_args.output_file
            )

        return 0

    except QRCodeError as e:
        # 处理自定义异常
        print(f"❌ 错误：{e}")
        return 1
    except KeyboardInterrupt:
        # 处理用户中断
        print("\n⚠️  操作已取消")
        return 130
    except Exception as e:
        # 处理其他未预期的异常
        print(f"❌ 执行失败：{e}")
        return 1
