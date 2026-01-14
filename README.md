# qrcode49

根据输入文件类型自动切换的二维码生成与解析工具。

## 功能

- **智能识别**：根据输入文件类型自动判断是生成二维码还是解析二维码
- **简单易用**：一条命令完成所有操作
- **多格式支持**：支持 PNG、JPG、WEBP 等多种图片格式

## 安装

```bash
# 使用 uv 安装
uv tool install git+https://github.com/Nine499/qrcode49.git

# 或本地安装
git clone git@github.com:Nine499/qrcode49.git
cd qrcode49
uv build
uv tool install dist/qrcode49-*.whl
```

## 使用方法

### 基本语法

```bash
qrcode49 <输入文件> <输出文件> [边长]
```

### 生成二维码

将文本文件转换为二维码图片：

```bash
# 生成 PNG 格式
qrcode49 input.txt output.png

# 生成 JPG 格式
qrcode49 input.txt output.jpg

# 生成 WEBP 格式
qrcode49 input.txt output.webp

# 自定义边长（默认 10）
qrcode49 input.txt output.png 20
```

### 解析二维码

从二维码图片中提取文本内容：

```bash
qrcode49 input.png output.txt
```

## 支持的文件格式

| 操作 | 输入格式 | 输出格式 |
|------|----------|----------|
| 生成二维码 | .txt, .md | .png, .jpg, .webp |
| 解析二维码 | .png, .jpg, .webp | .txt, .md |

## 使用示例

### 示例 1：生成网址二维码

```bash
echo "https://example.com" > url.txt
qrcode49 url.txt qr.png
```

### 示例 2：解析二维码

```bash
qrcode49 qr.png decoded.txt
cat decoded.txt
```

### 示例 3：调整二维码大小

```bash
# 边长越大，二维码图片越大
qrcode49 message.txt large.png 20
```

## 参数说明

| 参数 | 说明 | 必填 | 默认值 |
|------|------|------|--------|
| input_file | 输入文件路径 | 是 | - |
| output_file | 输出文件路径 | 是 | - |
| box_size | 二维码边长（每个模块的像素大小） | 否 | 10 |

## 技术栈

- Python 3.12+
- qrcode：二维码生成
- opencv-python：二维码解析
- pillow：图像处理

## 许可证

MIT License