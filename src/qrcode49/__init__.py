"""
qrcode49 - 二维码生成与解析工具包

这是一个智能的二维码工具包，支持：
- 二维码生成（从文本文件）
- 二维码解析（从图片文件）
- 命令行工具
- Python 库模式

使用示例（命令行）：
    $ qrcode49 input.txt output.png
    $ qrcode49 input.png output.txt

使用示例（Python 库）：
    >>> from qrcode49 import QRCodeGenerator, QRCodeDecoder
    >>>
    >>> # 生成二维码
    >>> generator = QRCodeGenerator(box_size=10)
    >>> generator.generate("Hello World", "output.png")
    >>>
    >>> # 解析二维码
    >>> decoder = QRCodeDecoder()
    >>> content = decoder.decode("qrcode.png")
    >>> print(content)
"""

__version__ = "2026.01.21.153342"

# 导出核心类和函数，方便用户使用
from qrcode49.config import (
    DEFAULT_BACK_COLOR,
    DEFAULT_BORDER,
    DEFAULT_BOX_SIZE,
    DEFAULT_ENCODING,
    DEFAULT_ERROR_CORRECTION,
    DEFAULT_FILL_COLOR,
    DEFAULT_VERSION,
    IMAGE_EXTENSIONS,
    MAX_BOX_SIZE,
    MIN_BOX_SIZE,
    TEXT_EXTENSIONS,
)
from qrcode49.decoder import QRCodeDecoder
from qrcode49.exceptions import (
    DecodeError,
    FileValidationError,
    GenerationError,
    ParameterError,
    QRCodeError,
)
from qrcode49.generator import QRCodeGenerator
from qrcode49.validators import (
    is_image_file,
    is_text_file,
    validate_box_size,
    validate_file_exists,
    validate_file_readable,
    validate_file_type_supported,
    validate_is_file,
    validate_output_format,
)

# 定义公开的 API
__all__ = [
    # 版本号
    "__version__",
    # 核心类
    "QRCodeGenerator",
    "QRCodeDecoder",
    # 异常类
    "QRCodeError",
    "FileValidationError",
    "DecodeError",
    "GenerationError",
    "ParameterError",
    # 配置常量
    "DEFAULT_BOX_SIZE",
    "DEFAULT_BORDER",
    "DEFAULT_VERSION",
    "DEFAULT_ERROR_CORRECTION",
    "DEFAULT_FILL_COLOR",
    "DEFAULT_BACK_COLOR",
    "DEFAULT_ENCODING",
    "MIN_BOX_SIZE",
    "MAX_BOX_SIZE",
    "TEXT_EXTENSIONS",
    "IMAGE_EXTENSIONS",
    # 验证函数
    "is_text_file",
    "is_image_file",
    "validate_box_size",
    "validate_file_exists",
    "validate_file_readable",
    "validate_file_type_supported",
    "validate_is_file",
    "validate_output_format",
]