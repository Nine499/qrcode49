"""
文件验证模块

该模块提供各种文件验证功能，确保输入文件符合要求。
"""

import os
from pathlib import Path

from qrcode49.config import IMAGE_EXTENSIONS, TEXT_EXTENSIONS
from qrcode49.exceptions import FileValidationError, ParameterError


def validate_file_exists(file_path: str) -> None:
    """
    验证文件是否存在

    Args:
        file_path: 文件路径

    Raises:
        FileValidationError: 如果文件不存在
    """
    if not os.path.exists(file_path):
        raise FileValidationError(
            f"输入文件不存在：{file_path}",
            "请检查文件路径是否正确，或确认文件是否已被删除"
        )


def validate_is_file(file_path: str) -> None:
    """
    验证路径是否为文件（而非目录）

    Args:
        file_path: 文件路径

    Raises:
        FileValidationError: 如果路径不是文件
    """
    if not os.path.isfile(file_path):
        raise FileValidationError(
            f"路径不是文件：{file_path}",
            "请确保输入的是文件路径，而不是目录路径"
        )


def validate_file_readable(file_path: str) -> None:
    """
    验证文件是否可读

    Args:
        file_path: 文件路径

    Raises:
        FileValidationError: 如果文件不可读
    """
    if not os.access(file_path, os.R_OK):
        raise FileValidationError(
            f"文件不可读：{file_path}",
            "请检查文件权限，确保当前用户有读取权限"
        )


def validate_text_file_not_empty(file_path: str) -> None:
    """
    验证文本文件是否为空

    Args:
        file_path: 文本文件路径

    Raises:
        FileValidationError: 如果文件为空
    """
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        raise FileValidationError(
            f"文本文件为空：{file_path}",
            "请确保文件中包含内容"
        )


def is_text_file(file_path: str) -> bool:
    """
    判断文件是否为文本文件

    Args:
        file_path: 文件路径

    Returns:
        如果是文本文件返回 True，否则返回 False
    """
    return Path(file_path).suffix.lower() in TEXT_EXTENSIONS


def is_image_file(file_path: str) -> bool:
    """
    判断文件是否为图片文件

    Args:
        file_path: 文件路径

    Returns:
        如果是图片文件返回 True，否则返回 False
    """
    return Path(file_path).suffix.lower() in IMAGE_EXTENSIONS


def validate_box_size(box_size: int) -> None:
    """
    验证边长参数是否在合理范围内

    Args:
        box_size: 边长参数

    Raises:
        ParameterError: 如果边长参数超出范围
    """
    from qrcode49.config import MAX_BOX_SIZE, MIN_BOX_SIZE

    if box_size < MIN_BOX_SIZE:
        raise ParameterError(
            f"边长参数必须大于等于 {MIN_BOX_SIZE}，当前值：{box_size}",
            f"请使用 {MIN_BOX_SIZE} 到 {MAX_BOX_SIZE} 之间的数值"
        )

    if box_size > MAX_BOX_SIZE:
        raise ParameterError(
            f"边长参数必须小于等于 {MAX_BOX_SIZE}，当前值：{box_size}",
            f"请使用 {MIN_BOX_SIZE} 到 {MAX_BOX_SIZE} 之间的数值"
        )


def validate_output_format(input_file: str, output_file: str) -> None:
    """
    验证输出文件格式是否与输入类型匹配

    Args:
        input_file: 输入文件路径
        output_file: 输出文件路径

    Raises:
        ParameterError: 如果输出格式不匹配
    """
    # 文本输入 → 图片输出
    if is_text_file(input_file) and not is_image_file(output_file):
        raise ParameterError(
            f"输出文件必须是图片格式，当前格式：{Path(output_file).suffix}",
            "请使用 .png、.jpg 或 .webp 格式作为输出文件"
        )

    # 图片输入 → 文本输出
    if is_image_file(input_file) and not is_text_file(output_file):
        raise ParameterError(
            f"输出文件必须是文本格式，当前格式：{Path(output_file).suffix}",
            "请使用 .txt 或 .md 格式作为输出文件"
        )


def validate_file_type_supported(file_path: str) -> None:
    """
    验证文件类型是否被支持

    Args:
        file_path: 文件路径

    Raises:
        FileValidationError: 如果文件类型不被支持
    """
    if not (is_text_file(file_path) or is_image_file(file_path)):
        raise FileValidationError(
            f"不支持的文件类型：{Path(file_path).suffix}",
            "支持的输入格式：.txt、.md、.png、.jpg、.jpeg、.webp"
        )