from __future__ import annotations

import sys
from pathlib import Path

import cv2
import qrcode

TEXT_SUFFIXES = {".md", ".txt"}
IMAGE_SUFFIXES = {".jpg", ".png", ".webp"}
DEFAULT_SIZE = 512


def detect_mode(input_path: Path) -> str:
    suffix = input_path.suffix.lower()
    if suffix in TEXT_SUFFIXES:
        return "encode"
    if suffix in IMAGE_SUFFIXES:
        return "decode"
    raise ValueError("参数1后缀不受支持")


def confirm_overwrite(output_path: Path) -> None:
    if not output_path.exists():
        return
    answer = input(f"{output_path} 已存在，是否覆盖? [y/N]: ").strip().lower()
    if answer != "y":
        raise FileExistsError("用户取消覆盖")


def read_text_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text_utf8(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def run_encode(input_path: Path, output_path: Path, size_arg: str | None) -> None:
    if output_path.suffix.lower() not in IMAGE_SUFFIXES:
        raise ValueError("生成模式的参数2必须是 jpg/png/webp")

    size = DEFAULT_SIZE
    if size_arg is not None:
        if not size_arg.isdigit():
            raise ValueError("参数3必须是纯数字")
        size = int(size_arg)
        if size <= 0:
            raise ValueError("参数3必须大于0")

    content = read_text_utf8(input_path)
    confirm_overwrite(output_path)

    qr_image = qrcode.make(content)
    image = qr_image.get_image().convert("RGB").resize((size, size))
    image.save(output_path)


def run_decode(input_path: Path, output_path: Path, size_arg: str | None) -> None:
    if size_arg is not None:
        raise ValueError("解析模式禁止提供参数3")
    if output_path.suffix.lower() not in TEXT_SUFFIXES:
        raise ValueError("解析模式的参数2必须是 md/txt")

    confirm_overwrite(output_path)

    image = cv2.imread(str(input_path), cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("无法读取图片")

    detector = cv2.QRCodeDetector()
    content, points, _ = detector.detectAndDecode(image)
    if points is None or content == "":
        raise ValueError("二维码解析失败")

    write_text_utf8(output_path, content)


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) not in (2, 3):
        raise ValueError("参数数量必须是2或3")

    input_path = Path(args[0])
    output_path = Path(args[1])
    size_arg = args[2] if len(args) == 3 else None

    if not input_path.exists():
        raise FileNotFoundError("参数1文件不存在")

    mode = detect_mode(input_path)
    if mode == "encode":
        run_encode(input_path, output_path, size_arg)
        return
    run_decode(input_path, output_path, size_arg)
