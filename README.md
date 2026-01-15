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
- ✅ **错误处理**：完善的输入验证和友好的错误提示

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
├── uv.lock                 # 依赖锁定文件
├── README.md               # 项目文档
├── 给AI的需求.md            # 需求文档
├── dist/                   # 构建输出目录
└── src/
    └── qrcode49/
        ├── __init__.py     # 包初始化文件
        └── main.py         # 主程序入口
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

### 示例 1：生成个人名片二维码

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

### 示例 2：批量生成二维码

```bash
# 使用循环批量处理
for file in data/*.txt; do
  qrcode49 "$file" "output/$(basename $file .txt).png"
done
```

### 示例 3：解析二维码内容

```bash
# 解析二维码
qrcode49 qrcode.png content.txt

# 查看内容
cat content.txt
```

---

## 🐛 常见问题

### Q: 生成的二维码图片太大怎么办？

A: 减小 `box_size` 参数值，例如使用 `5` 或 `8`。

### Q: 解析二维码失败怎么办？

A: 确保图片清晰，二维码完整，没有遮挡或反光。

### Q: 支持哪些图片格式？

A: 目前支持 PNG、JPG、JPEG、WebP 格式。

### Q: 可以生成彩色二维码吗？

A: 当前版本仅支持黑白二维码，未来版本可能会增加彩色支持。

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