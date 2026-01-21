"""
自定义异常类模块

该模块定义了项目中所有自定义异常类，用于提供更精确的错误信息和更好的错误处理。
"""


class QRCodeError(Exception):
    """
    二维码错误基类

    所有二维码相关的自定义异常都应该继承自这个基类。
    这使得在 CLI 层可以统一捕获和处理所有二维码相关的错误。
    """

    def __init__(self, message: str, suggestion: str = "") -> None:
        """
        初始化异常

        Args:
            message: 错误信息
            suggestion: 解决建议（可选）
        """
        self.message = message
        self.suggestion = suggestion
        super().__init__(self.message)

    def __str__(self) -> str:
        """返回格式化的错误信息"""
        if self.suggestion:
            return f"{self.message}\n💡 建议：{self.suggestion}"
        return self.message


class FileValidationError(QRCodeError):
    """
    文件验证错误

    当输入文件不符合要求时抛出此异常，例如：
    - 文件不存在
    - 文件格式不支持
    - 文件为空
    - 文件权限不足
    """

    pass


class DecodeError(QRCodeError):
    """
    二维码解析错误

    当解析二维码失败时抛出此异常，例如：
    - 图片中未检测到二维码
    - 二维码损坏或模糊
    - 二维码数据格式错误
    """

    pass


class GenerationError(QRCodeError):
    """
    二维码生成错误

    当生成二维码失败时抛出此异常，例如：
    - 文本内容过长
    - 参数配置错误
    - 图片保存失败
    """

    pass


class ParameterError(QRCodeError):
    """
    参数错误

    当命令行参数或函数参数不符合要求时抛出此异常，例如：
    - 边长参数超出范围
    - 输出文件格式不匹配
    - 缺少必需参数
    """

    pass
