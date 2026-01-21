# qrcode49

根据输入文件类型自动切换的二维码生成与解析工具

---

## 📋 项目简介

一个智能的命令行工具，能够根据输入文件类型自动识别并执行对应的二维码操作：

- 📄 **文本文件** → 生成二维码图片
- 🖼️ **图片文件** → 解析二维码内容

---

## ✨ 功能特性

- ✅ **智能识别**：根据文件扩展名自动切换生成/解析模式
- ✅ **生成二维码**：将文本内容转换为高质量二维码图片
- ✅ **解析二维码**：从图片中快速提取二维码内容
- ✅ **自定义边长**：可调整二维码模块大小，控制图片尺寸
- ✅ **多格式支持**：支持 TXT、MD、PNG、JPG、WebP 等多种格式
- ✅ **错误处理**：完善的输入验证和友好的错误提示，包含解决建议
- ✅ **库模式支持**：可作为 Python 库在其他程序中使用
- ✅ **中文支持**：完美支持中文文本和特殊字符
- ✅ **模块化设计**：代码结构清晰，易于维护和扩展

---

## 🔧 环境要求

- **Python**: >= 3.12
- **操作系统**: Linux / macOS / Windows

---

## 📦 安装指南

### 方式一：使用 uv tool 安装（推荐）

```bash
uv tool install qrcode49
```

### 方式二：使用 pip 安装

```bash
pip install qrcode49
```

### 方式三：从源码安装

```bash
# 克隆仓库
git clone https://github.com/Nine499/qrcode49.git
cd qrcode49

# 使用 uv 安装
uv pip install -e .

# 或使用 pip 安装
pip install -e .
```

### 方式四：从本地构建

```bash
# 构建项目
uv build

# 安装构建产物
uv tool install dist/qrcode49-*.whl
```

---

## 🚀 快速开始

### 生成二维码

将文本文件转换为二维码图片：

```bash
# 默认边长（10）
qrcode49 input.txt output.png

# 自定义边长（20）
qrcode49 input.txt output.png 20

# 使用 Markdown 文件
qrcode49 README.md qrcode.png
```

### 解析二维码

从图片中提取二维码内容：

```bash
# 解析 PNG 图片
qrcode49 input.png output.txt

# 解析 JPG 图片
qrcode49 qrcode.jpg content.txt

# 解析 WebP 图片
qrcode49 qrcode.webp content.txt
```

### 查看帮助

```bash
qrcode49 --help
```

---

## 📖 使用说明

### 命令行参数

| 参数 | 说明 | 必填 | 默认值 |
|------|------|------|--------|
| `input_file` | 输入文件路径（文本或图片） | ✅ 是 | - |
| `output_file` | 输出文件路径 | ✅ 是 | - |
| `box_size` | 二维码模块像素大小 | ❌ 否 | 10 |

### 边长参数说明

- **默认值**：10
- **推荐范围**：1-50
- **影响**：边长越大，二维码图片越大，但扫描识别度可能降低
- **示例**：
  - `box_size=5` → 小尺寸二维码，适合打印在名片上
  - `box_size=10` → 标准尺寸二维码（默认）
  - `box_size=20` → 大尺寸二维码，适合远距离扫描

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
- 文本输入 → 图片输出（PNG、JPG、WebP）
- 图片输入 → 文本输出（TXT、MD）

---

## 📂 项目结构

```
qrcode49/
├── .gitignore              # Git 忽略文件
├── .python-version         # Python 版本配置
├── pyproject.toml          # 项目配置文件
├── README.md               # 项目文档
├── AGENTS.md               # AI 上下文文档
├── orchestrator.md         # 指挥日志
└── src/qrcode49/
    ├── __init__.py         # 包初始化文件，导出 API
    ├── config.py           # 配置和常量管理
    ├── exceptions.py       # 自定义异常类
    ├── validators.py       # 文件验证逻辑
    ├── generator.py        # 二维码生成器（面向对象）
    ├── decoder.py          # 二维码解析器（面向对象）
    ├── cli.py              # 命令行接口
    └── main.py             # 主程序入口
```

---

## 🛠️ 依赖项

| 包名 | 版本要求 | 用途 |
|------|----------|------|
| opencv-python | >= 4.12.0.88 | 二维码解析 |
| pillow | >= 12.1.0 | 图片处理 |
| qrcode | >= 8.2 | 二维码生成 |

---

## 💡 使用示例

### 命令行使用

#### 示例 1：生成个人名片二维码

```bash
# 创建名片信息
cat > card.txt << EOF
姓名：张三
电话：138-0000-0000
邮箱：zhangsan@example.com
EOF

# 生成二维码
qrcode49 card.txt card.png 15
```

#### 示例 2：批量生成二维码

```bash
# 使用循环批量处理
for file in data/*.txt; do
  qrcode49 "$file" "output/$(basename $file .txt).png"
done
```

#### 示例 3：解析二维码内容

```bash
# 解析二维码
qrcode49 qrcode.png content.txt

# 查看内容
cat content.txt
```

### Python 库使用

#### 示例 1：生成二维码

```python
from qrcode49 import QRCodeGenerator

# 创建生成器
generator = QRCodeGenerator(box_size=10)

# 生成二维码
generator.generate("Hello, World!", "output.png")

# 从文件生成
generator.generate_from_file("input.txt", "output.png")
```

#### 示例 2：解析二维码

```python
from qrcode49 import QRCodeDecoder

# 创建解析器
decoder = QRCodeDecoder()

# 解析二维码
content = decoder.decode("qrcode.png")
print(content)

# 解析并保存到文件
decoder.decode_to_file("qrcode.png", "output.txt")
```

#### 示例 3：自定义参数

```python
from qrcode49 import QRCodeGenerator

# 创建生成器，自定义参数
generator = QRCodeGenerator(
    box_size=15,              # 边长
    border=4,                 # 边框
    error_correction='H',     # 纠错级别
    fill_color="black",       # 二维码颜色
    back_color="white"        # 背景颜色
)

# 生成二维码
generator.generate("自定义二维码", "custom.png")
```

---

## 🐛 常见问题

### Q: 生成的二维码图片太大怎么办？

A: 减小 `box_size` 参数值，例如使用 `5` 或 `8`。

### Q: 解析二维码失败怎么办？

A: 确保图片清晰，二维码完整，没有遮挡或反光。错误信息会提供具体的解决建议。

### Q: 支持哪些图片格式？

A: 目前支持 PNG、JPG、JPEG、WebP 格式。

### Q: 可以生成彩色二维码吗？

A: 当前版本仅支持黑白二维码，但可以通过 Python 库自定义颜色。

### Q: 如何在 Python 代码中使用？

A: 导入 `QRCodeGenerator` 和 `QRCodeDecoder` 类即可，详见上面的"Python 库使用"示例。

### Q: 支持中文吗？

A: 完全支持中文文本和特殊字符。

### Q: 二维码能存储多少内容？

A: 取决于二维码版本和纠错级别，通常可以存储几百到几千个字符。

---

## 📄 许可证

MIT License

---

## 👨‍💻 作者

Nine499

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📞 联系方式

- GitHub: https://github.com/Nine499/qrcode49
- Issues: https://github.com/Nine499/qrcode49/issues