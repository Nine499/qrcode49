"""二维码核心功能"""

from pathlib import Path
from qrcode import QRCode, constants, decode as qr_decode
from PIL import Image
from qrcode49.config import (
    DEFAULT_BOX_SIZE,
    DEFAULT_BORDER,
    DEFAULT_VERSION,
    DEFAULT_ERROR_CORRECTION,
    DEFAULT_FILL_COLOR,
    DEFAULT_BACK_COLOR,
)


def generate_qrcode(
    text: str,
    output_path: str,
    box_size: int = DEFAULT_BOX_SIZE,
    border: int = DEFAULT_BORDER,
    version: int = DEFAULT_VERSION,
    error_correction: str = DEFAULT_ERROR_CORRECTION,
    fill_color: str = DEFAULT_FILL_COLOR,
    back_color: str = DEFAULT_BACK_COLOR,
) -> None:
    """生成二维码图片

    Args:
        text: 要编码的文本内容
        output_path: 输出图片路径
        box_size: 二维码每个模块的像素大小
        border: 二维码边框宽度
        version: 二维码版本号
        error_correction: 纠错级别 ('L', 'M', 'Q', 'H')
        fill_color: 二维码颜色
        back_color: 背景颜色

    Raises:
        ValueError: 如果文本为空或参数无效
    """
    if not text:
        raise ValueError("文本内容不能为空")

    # 纠错级别映射
    level_map = {
        "L": constants.ERROR_CORRECT_L,
        "M": constants.ERROR_CORRECT_M,
        "Q": constants.ERROR_CORRECT_Q,
        "H": constants.ERROR_CORRECT_H,
    }

    if error_correction not in level_map:
        raise ValueError(f"无效的纠错级别: {error_correction}")

    try:
        # 创建二维码
        qr = QRCode(
            version=version,
            error_correction=level_map[error_correction],
            box_size=box_size,
            border=border,
        )
        qr.add_data(text)
        qr.make(fit=True)

        # 生成图片
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # JPEG 格式需要 RGB 模式
        if Path(output_path).suffix.lower() in {".jpg", ".jpeg"}:
            img = img.convert("RGB")

        img.save(output_path)

    except Exception as e:
        raise ValueError(f"生成二维码失败: {e}")


def decode_qrcode(image_path: str) -> str:
    """解析二维码图片

    Args:
        image_path: 输入图片路径

    Returns:
        二维码中的文本内容

    Raises:
        FileNotFoundError: 如果图片文件不存在
        ValueError: 如果解析失败
    """
    if not Path(image_path).exists():
        raise FileNotFoundError(f"图片文件不存在: {image_path}")

    try:
        # 打开图片
        img = Image.open(image_path)

        # 解码二维码
        decoded_list = qr_decode(img)

        if not decoded_list:
            raise ValueError("未在图片中检测到二维码")

        # 返回第一个解码结果
        return decoded_list[0].data.decode("utf-8")

    except Exception as e:
        raise ValueError(f"解析二维码失败: {e}")
