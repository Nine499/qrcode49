"""
配置和常量管理模块

该模块集中管理项目中所有的配置参数和常量定义，便于统一维护和修改。
"""

from typing import Final, Set

# 支持的文本文件扩展名
TEXT_EXTENSIONS: Final[Set[str]] = {'.txt', '.md'}

# 支持的图片文件扩展名
IMAGE_EXTENSIONS: Final[Set[str]] = {'.png', '.jpg', '.jpeg', '.webp'}

# 二维码默认配置
DEFAULT_BOX_SIZE: Final[int] = 10  # 默认边长（每个模块的像素大小）
DEFAULT_BORDER: Final[int] = 4     # 默认边框宽度
DEFAULT_VERSION: Final[int] = 1    # 默认版本号（自动调整）

# 二维码纠错级别
# ERROR_CORRECT_L: 约 7% 的纠错能力
# ERROR_CORRECT_M: 约 15% 的纠错能力
# ERROR_CORRECT_Q: 约 25% 的纠错能力
# ERROR_CORRECT_H: 约 30% 的纠错能力
DEFAULT_ERROR_CORRECTION: Final[str] = 'L'

# 边长参数的推荐范围
MIN_BOX_SIZE: Final[int] = 1   # 最小边长
MAX_BOX_SIZE: Final[int] = 50  # 最大边长

# 二维码颜色配置
DEFAULT_FILL_COLOR: Final[str] = "black"   # 二维码颜色
DEFAULT_BACK_COLOR: Final[str] = "white"   # 背景颜色

# 文件编码
DEFAULT_ENCODING: Final[str] = 'utf-8'