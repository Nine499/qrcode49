"""qrcode49 - 简洁友好的二维码工具"""

__version__ = "2026.01.21.153342"

from qrcode49.core import generate_qrcode, decode_qrcode
from qrcode49.config import (
    TEXT_EXTENSIONS,
    IMAGE_EXTENSIONS,
    DEFAULT_BOX_SIZE,
    DEFAULT_BORDER,
    DEFAULT_VERSION,
    DEFAULT_ERROR_CORRECTION,
    DEFAULT_FILL_COLOR,
    DEFAULT_BACK_COLOR,
    DEFAULT_ENCODING,
)

__all__ = [
    "__version__",
    "generate_qrcode",
    "decode_qrcode",
    "TEXT_EXTENSIONS",
    "IMAGE_EXTENSIONS",
    "DEFAULT_BOX_SIZE",
    "DEFAULT_BORDER",
    "DEFAULT_VERSION",
    "DEFAULT_ERROR_CORRECTION",
    "DEFAULT_FILL_COLOR",
    "DEFAULT_BACK_COLOR",
    "DEFAULT_ENCODING",
]
