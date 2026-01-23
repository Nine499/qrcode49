# qrcode49

简洁友好的二维码生成与解析工具

## 特性

- 🎯 **双模式**: 支持交互式向导和命令行两种模式
- 🚀 **简单易用**: 新手友好的交互式引导
- ⚡ **快速**: 精简依赖，安装迅速
- 🔧 **灵活**: 支持多种文件格式

## 安装

```bash
# 使用 uv
uv sync

# 或安装为本地包
uv pip install -e .
```

## 使用方法

### 交互式向导模式（推荐新手）

```bash
uv run qrcode49
```

按照提示逐步完成操作。

### 命令行模式

#### 生成二维码

```bash
uv run qrcode49 input.txt output.png
```

#### 解析二维码

```bash
uv run qrcode49 input.png output.txt
```

#### 自定义二维码大小

```bash
uv run qrcode49 input.txt output.png 15
```

## 支持的格式

**文本输入**: `.txt`, `.md`

**图片输入**: `.png`, `.jpg`, `.jpeg`, `.webp`

## Python API

```python
from qrcode49 import generate_qrcode, decode_qrcode

# 生成二维码
generate_qrcode("Hello World", "qrcode.png")

# 解析二维码
content = decode_qrcode("qrcode.png")
print(content)
```

## 开发

```bash
# 安装依赖
uv sync

# 运行
uv run qrcode49

# 构建
uv build
```

## 许可证

MIT