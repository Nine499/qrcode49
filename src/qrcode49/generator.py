"""
二维码生成器模块

该模块提供二维码生成功能，支持面向对象的方式调用。
"""

from pathlib import Path

import qrcode

from qrcode49.config import (
    DEFAULT_BACK_COLOR,
    DEFAULT_BORDER,
    DEFAULT_BOX_SIZE,
    DEFAULT_ERROR_CORRECTION,
    DEFAULT_FILL_COLOR,
    DEFAULT_VERSION,
)
from qrcode49.exceptions import GenerationError


class QRCodeGenerator:
    """
    二维码生成器类

    该类封装了二维码生成的所有逻辑，支持灵活的配置参数。

    使用示例：
        >>> generator = QRCodeGenerator(box_size=15)
        >>> generator.generate("Hello World", "output.png")
    """

    def __init__(
        self,
        box_size: int = DEFAULT_BOX_SIZE,
        border: int = DEFAULT_BORDER,
        version: int = DEFAULT_VERSION,
        error_correction: str = DEFAULT_ERROR_CORRECTION,
        fill_color: str = DEFAULT_FILL_COLOR,
        back_color: str = DEFAULT_BACK_COLOR,
    ) -> None:
        """
        初始化二维码生成器

        Args:
            box_size: 二维码每个模块的像素大小（边长参数）
            border: 二维码边框宽度（模块数）
            version: 二维码版本号（1-40），1 表示最小尺寸，40 表示最大尺寸
            error_correction: 纠错级别（'L', 'M', 'Q', 'H'）
            fill_color: 二维码颜色
            back_color: 背景颜色
        """
        self.box_size = box_size
        self.border = border
        self.version = version
        self.error_correction = error_correction
        self.fill_color = fill_color
        self.back_color = back_color

        # 将纠错级别字符串转换为 qrcode 常量
        self._error_correction_level = self._get_error_correction_level(error_correction)

    def _get_error_correction_level(self, level: str) -> int:
        """
        将纠错级别字符串转换为 qrcode 常量

        Args:
            level: 纠错级别字符串（'L', 'M', 'Q', 'H'）

        Returns:
            qrcode 纠错级别常量

        Raises:
            GenerationError: 如果纠错级别无效
        """
        level_map = {
            'L': qrcode.constants.ERROR_CORRECT_L,
            'M': qrcode.constants.ERROR_CORRECT_M,
            'Q': qrcode.constants.ERROR_CORRECT_Q,
            'H': qrcode.constants.ERROR_CORRECT_H,
        }

        if level not in level_map:
            raise GenerationError(
                f"无效的纠错级别：{level}",
                "请使用 'L'、'M'、'Q' 或 'H' 中的一个"
            )

        return level_map[level]

    def generate(self, text: str, output_path: str) -> None:
        """
        生成二维码图片

        Args:
            text: 要编码的文本内容
            output_path: 输出图片路径

        Raises:
            GenerationError: 如果生成失败
        """
        if not text:
            raise GenerationError(
                "文本内容不能为空",
                "请提供有效的文本内容"
            )

        try:
            # 创建 QRCode 对象
            qr = qrcode.QRCode(
                version=self.version,
                error_correction=self._error_correction_level,
                box_size=self.box_size,
                border=self.border,
            )

            # 添加数据并生成二维码
            qr.add_data(text)
            qr.make(fit=True)

            # 生成图片
            img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)

            # JPEG 格式需要转换为 RGB 模式
            output_ext = Path(output_path).suffix.lower()
            if output_ext in {'.jpg', '.jpeg'}:
                img = img.convert('RGB')

            # 保存图片
            img.save(output_path)

        except Exception as e:
            raise GenerationError(
                f"生成二维码失败：{str(e)}",
                "请检查文本内容是否过长，或尝试减小边长参数"
            )

    def generate_from_file(self, input_path: str, output_path: str, encoding: str = 'utf-8') -> None:
        """
        从文本文件生成二维码

        Args:
            input_path: 输入文本文件路径
            output_path: 输出图片路径
            encoding: 文件编码，默认为 utf-8

        Raises:
            GenerationError: 如果生成失败
        """
        try:
            with open(input_path, 'r', encoding=encoding) as f:
                text_content = f.read()

            self.generate(text_content, output_path)

        except UnicodeDecodeError:
            raise GenerationError(
                f"文件编码错误：{input_path}",
                f"请确保文件使用 {encoding} 编码，或指定正确的编码格式"
            )
        except Exception as e:
            raise GenerationError(
                f"读取文件失败：{str(e)}",
                "请检查文件路径和权限"
            )