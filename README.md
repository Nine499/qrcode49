# qrcode49

一个简单易用的命令行二维码生成与解析工具，根据输入文件类型自动切换功能。

## 功能特性

- **智能识别**：根据输入文件类型自动判断是生成二维码还是解析二维码
- **多格式支持**：支持 PNG、JPG、WEBP、SVG 等多种图片格式
- **纯 Python 实现**：无需系统依赖，跨平台兼容
- **简单易用**：一条命令完成所有操作

## 安装

### 前置要求

- Python 3.12 或更高版本
- [uv](https://github.com/astral-sh/uv) 包管理工具

### 安装步骤

```bash
# 克隆项目
git clone <repository-url>
cd qrcode49

# 同步依赖
uv sync
```

## 使用方法

### 基本语法

```bash
uv run python src/qrcode49/main.py <输入文件> <输出文件>
```

### 生成二维码

将文本文件转换为二维码图片：

```bash
# 生成 PNG 格式
uv run python src/qrcode49/main.py input.txt output.png

# 生成 JPG 格式
uv run python src/qrcode49/main.py input.txt output.jpg

# 生成 WEBP 格式
uv run python src/qrcode49/main.py input.txt output.webp

# 生成 SVG 矢量图
uv run python src/qrcode49/main.py input.txt output.svg
```

### 解析二维码

从二维码图片中提取文本内容：

```bash
uv run python src/qrcode49/main.py input.png output.txt
```

## 支持的文件格式

### 输入文件

| 类型     | 支持格式                         | 说明           |
| -------- | -------------------------------- | -------------- |
| 文本文件 | `.txt`, `.md`                    | 用于生成二维码 |
| 图片文件 | `.png`, `.jpg`, `.jpeg`, `.webp` | 用于解析二维码 |

### 输出文件

| 类型     | 支持格式                        | 说明             |
| -------- | ------------------------------- | ---------------- |
| 图片文件 | `.png`, `.jpg`, `.webp`, `.svg` | 二维码图片       |
| 文本文件 | `.txt`, `.md`                   | 解析后的文本内容 |

**注意**：SVG 格式仅支持生成，不支持解析。

## 使用示例

### 示例 1：生成网址二维码

```bash
# 创建文本文件
echo "https://example.com" > url.txt

# 生成二维码
uv run python src/qrcode49/main.py url.txt qr.png
```

### 示例 2：解析二维码

```bash
# 解析二维码图片
uv run python src/qrcode49/main.py qr.png decoded.txt

# 查看解析结果
cat decoded.txt
```

### 示例 3：批量处理

```bash
# 生成多个格式的二维码
uv run python src/qrcode49/main.py message.txt message.png
uv run python src/qrcode49/main.py message.txt message.jpg
uv run python src/qrcode49/main.py message.txt message.svg
```

## 项目结构

```
qrcode49/
├── pyproject.toml          # 项目配置文件
├── README.md               # 项目说明文档
└── src/
    └── qrcode49/
        ├── __init__.py     # 包初始化文件
        └── main.py         # 主程序入口
```

## 技术栈

- **Python**: 3.12+
- **包管理**: uv
- **二维码生成**: qrcode
- **二维码解析**: opencv-python
- **图像处理**: pillow

## 依赖项

```toml
opencv-python>=4.12.0.88
qrcode[pil]>=8.2
```

## 常见问题

### Q: 为什么 SVG 格式不能解析？

A: SVG 是矢量图格式，解析需要额外的系统依赖。为了保持纯 Python 实现和无系统依赖的特性，目前仅支持 SVG 生成，不支持解析。

### Q: 支持哪些二维码版本？

A: 使用 QR Code Model 2 标准，支持版本 1-40，自动根据内容大小选择合适的版本。

### Q: 生成的二维码有多大？

A: 默认大小为 10 像素/模块，边框为 4 个模块。可以通过修改代码中的 `box_size` 和 `border` 参数来调整。

## 开发

### 运行测试

```bash
# 生成测试二维码
uv run python src/qrcode49/main.py test.txt test.png

# 解析测试二维码
uv run python src/qrcode49/main.py test.png output.txt

# 验证结果
cat output.txt
```

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 作者

qrcode49 Development Team
