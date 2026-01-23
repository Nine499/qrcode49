# qrcode49

简洁友好的二维码生成与解析工具

## ✨ 特性

- 🎯 **双模式支持**：交互式向导模式（新手友好）和命令行模式（快速高效）
- 🚀 **简单易用**：清晰的步骤引导，智能的文件类型识别
- ⚡ **快速高效**：精简的依赖，优化的代码结构
- 🔧 **灵活配置**：支持自定义二维码大小、颜色等参数
- 🌐 **多格式支持**：支持 TXT、MD、PNG、JPG、JPEG、WebP 等格式
- 💬 **中文友好**：完整的中文界面和文档
- 📦 **纯 Python**：无系统依赖，跨平台支持

## 📋 环境要求

- **Python**: 3.12+
- **操作系统**: Linux / macOS / Windows

## 📦 安装

### 使用 uv（推荐）

```bash
# 克隆项目
git clone https://github.com/Nine499/qrcode49.git
cd qrcode49

# 安装依赖
uv sync

# 安装为本地包
uv pip install -e .
```

### 使用 pip

```bash
# 克隆项目
git clone https://github.com/Nine499/qrcode49.git
cd qrcode49

# 安装依赖
pip install -e .
```

## 🚀 快速开始

### 交互式向导模式（推荐新手）

```bash
uv run qrcode49
```

按照提示逐步完成操作：

```
🎯 二维码工具 - 交互式向导

请选择操作:
  1. 生成二维码（文本 → 图片）
  2. 解析二维码（图片 → 文本）

请输入选项 (1 或 2):
```

### 命令行模式

#### 生成二维码

```bash
# 默认大小
uv run qrcode49 input.txt output.png

# 自定义大小
uv run qrcode49 input.txt output.png 15
```

#### 解析二维码

```bash
uv run qrcode49 input.png output.txt
```

## 📖 使用说明

### 交互式向导模式

交互式模式提供了友好的引导界面，适合不熟悉命令行的新手用户：

1. **选择操作类型**：生成或解析二维码
2. **输入文件路径**：支持相对路径和绝对路径
3. **输出文件路径**：提供智能默认值
4. **配置参数**：按 Enter 使用默认值
5. **确认执行**：显示操作摘要，确认后才执行
6. **查看结果**：实时显示执行进度和结果

### 命令行模式

命令行模式适合脚本自动化和熟练用户使用：

#### 基本用法

```bash
qrcode49 <输入文件> <输出文件> [边长]
```

#### 参数说明

| 参数 | 说明 | 必填 | 默认值 |
|------|------|------|--------|
| `输入文件` | 文本文件或图片文件路径 | ✅ 是 | - |
| `输出文件` | 输出文件路径 | ✅ 是 | - |
| `边长` | 二维码模块像素大小 | ❌ 否 | 10 |

#### 边长参数说明

- **默认值**: 10
- **推荐范围**: 1-50
- **影响**: 边长越大，二维码图片越大
- **示例**:
  - `5` - 小尺寸，适合名片
  - `10` - 标准尺寸（默认）
  - `20` - 大尺寸，适合远距离扫描

### 支持的文件格式

#### 输入文件

**文本文件**（用于生成二维码）：
- `.txt` - 纯文本文件
- `.md` - Markdown 文件

**图片文件**（用于解析二维码）：
- `.png` - PNG 图片
- `.jpg` / `.jpeg` - JPEG 图片
- `.webp` - WebP 图片

#### 输出文件

根据输入文件类型自动匹配：
- 文本输入 → 图片输出（`.png`, `.jpg`, `.jpeg`, `.webp`）
- 图片输入 → 文本输出（`.txt`, `.md`）

## 💻 Python API

### 生成二维码

```python
from qrcode49 import generate_qrcode

# 基本用法
generate_qrcode("Hello World", "qrcode.png")

# 自定义参数
generate_qrcode(
    text="自定义内容",
    output_path="custom.png",
    box_size=15,              # 边长
    border=4,                 # 边框
    error_correction='H',     # 纠错级别
    fill_color="black",       # 二维码颜色
    back_color="white"        # 背景颜色
)
```

### 解析二维码

```python
from qrcode49 import decode_qrcode

# 基本用法
content = decode_qrcode("qrcode.png")
print(content)
```

### 可用的配置常量

```python
from qrcode49 import (
    TEXT_EXTENSIONS,          # 文本文件扩展名
    IMAGE_EXTENSIONS,         # 图片文件扩展名
    DEFAULT_BOX_SIZE,         # 默认边长
    DEFAULT_BORDER,           # 默认边框
    DEFAULT_VERSION,          # 默认版本
    DEFAULT_ERROR_CORRECTION, # 默认纠错级别
    DEFAULT_FILL_COLOR,       # 默认二维码颜色
    DEFAULT_BACK_COLOR,       # 默认背景颜色
    DEFAULT_ENCODING,         # 默认编码
)
```

## 🛠️ 开发

### 安装开发依赖

```bash
uv sync
```

### 运行项目

```bash
# 交互式模式
uv run qrcode49

# 命令行模式
uv run qrcode49 input.txt output.png
```

### 构建包

```bash
uv build
```

### 测试

```bash
# 测试生成
echo "测试内容" > test.txt
uv run qrcode49 test.txt test.png

# 测试解析
uv run qrcode49 test.png test_output.txt
cat test_output.txt

# 测试交互式模式
uv run qrcode49

# 清理
rm test.txt test.png test_output.txt
```

### 项目结构

```
qrcode49/
├── src/qrcode49/
│   ├── __init__.py    # 包初始化文件
│   ├── main.py        # 主程序入口
│   ├── core.py        # 核心功能
│   └── config.py      # 配置常量
├── pyproject.toml     # 项目配置
├── AGENTS.md          # AI Agent 指南
└── README.md          # 项目文档
```

## ❓ 常见问题

### Q1: 生成的二维码图片太大怎么办？

A: 减小边长参数，例如使用 `5` 或 `8`。

### Q2: 解析二维码失败怎么办？

A: 确保图片清晰，二维码完整，没有遮挡或反光。

### Q3: 支持哪些图片格式？

A: PNG、JPG、JPEG、WebP。

### Q4: 可以生成彩色二维码吗？

A: 当前版本仅支持黑白二维码，但可以通过 Python API 自定义颜色。

### Q5: 支持中文吗？

A: 完全支持中文文本和特殊字符。

### Q6: 二维码能存储多少内容？

A: 取决于二维码版本和纠错级别，通常可以存储几百到几千个字符。

### Q7: 如何在脚本中使用？

A: 导入 `generate_qrcode` 和 `decode_qrcode` 函数即可。

## 📄 许可证

MIT License

## 👨‍💻 作者

Nine499

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 联系方式

- GitHub: https://github.com/Nine499/qrcode49
- Issues: https://github.com/Nine499/qrcode49/issues

---

**享受使用 qrcode49！** 🎉