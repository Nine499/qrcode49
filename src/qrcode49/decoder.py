"""
二维码解析器模块

该模块提供二维码解析功能，支持面向对象的方式调用。
"""

import cv2
import numpy as np
from qrcode49.exceptions import DecodeError
from qrcode49.config import DEFAULT_ENCODING


class QRCodeDecoder:
    """
    二维码解析器类

    该类封装了二维码解析的所有逻辑，支持从图片中提取二维码内容。

    使用示例：
        >>> decoder = QRCodeDecoder()
        >>> content = decoder.decode("qrcode.png")
        >>> print(content)
    """

    def __init__(self) -> None:
        """初始化二维码解析器"""
        self.detector = cv2.QRCodeDetector()

    def decode(self, image_path: str) -> str:
        """
        解析图片中的二维码

        Args:
            image_path: 输入图片路径

        Returns:
            二维码中的文本内容

        Raises:
            DecodeError: 如果解析失败
        """
        try:
            # 读取图片
            img = cv2.imread(image_path)
            if img is None:
                raise DecodeError(
                    f"无法读取图片文件：{image_path}",
                    "请检查图片路径是否正确，或确认文件是否为有效的图片格式"
                )

            # 检测并解码二维码
            data, bbox, _ = self.detector.detectAndDecode(img)

            # 如果第一次尝试失败，尝试使用更宽松的参数
            if not data:
                data = self._decode_with_retry(img)

            if not data:
                raise DecodeError(
                    "未在图片中检测到二维码",
                    "请确保图片清晰，二维码完整可见，没有被遮挡或反光"
                )

            return data

        except DecodeError:
            # 重新抛出 DecodeError
            raise
        except Exception as e:
            raise DecodeError(
                f"解析二维码失败：{str(e)}",
                "请检查图片是否损坏，或尝试使用更清晰的图片"
            )

    def _decode_with_retry(self, img: np.ndarray) -> str:
        """
        使用更宽松的参数尝试解码二维码

        Args:
            img: OpenCV 图片对象

        Returns:
            解码后的文本内容，如果失败返回空字符串
        """
        # 尝试调整图片对比度和亮度
        try:
            # 增加对比度
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            if len(img.shape) == 3:
                # 彩色图片，转换为灰度图
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                enhanced = clahe.apply(gray)
            else:
                enhanced = clahe.apply(img)

            # 尝试解码增强后的图片
            data, _, _ = self.detector.detectAndDecode(enhanced)
            return data if data else ""

        except Exception:
            # 如果增强失败，返回空字符串
            return ""

    def decode_to_file(self, image_path: str, output_path: str, encoding: str = DEFAULT_ENCODING) -> None:
        """
        解析图片中的二维码并保存到文件

        Args:
            image_path: 输入图片路径
            output_path: 输出文本文件路径
            encoding: 输出文件编码，默认为 utf-8

        Raises:
            DecodeError: 如果解析失败
        """
        try:
            # 解析二维码
            content = self.decode(image_path)

            # 保存到文件
            with open(output_path, 'w', encoding=encoding) as f:
                f.write(content)

        except DecodeError:
            # 重新抛出 DecodeError
            raise
        except Exception as e:
            raise DecodeError(
                f"保存解析结果失败：{str(e)}",
                "请检查输出路径是否有写入权限"
            )