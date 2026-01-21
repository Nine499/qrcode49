# qrcode49 项目上下文文档

## 项目概述

**项目名称**: qrcode49  
**项目类型**: Python 命令行工具  
**当前版本**: 2026.01.15.091659  
**Python 要求**: >= 3.12

### 项目简介

qrcode49 是一个智能的命令行工具，能够根据输入文件类型自动识别并执行对应的二维码操作：

- **文本文件** (.txt, .md) → 生成二维码图片
- **图片文件** (.png, .jpg, .jpeg, .webp) → 解析二维码内容

### 核心功能

1. **智能识别**: 根据文件扩展名自动切换生成/解析模式
2. **生成二维码**: 将文本内容转换为高质量二维码图片
3. **解析二维码**: 从图片中快速提取二维码内容
4. **自定义边长**: 可调整二维码模块大小（box_size 参数），控制图片尺寸
5. **多格式支持**: 支持 TXT、MD、PNG、JPG、WebP 等多种格式
6. **错误处理**: 完善的输入验证和友好的错误提示

### 技术栈

- **语言**: Python 3.12+
- **核心依赖**:
  - `opencv-python` >= 4.12.0.88 - 二维码解析
  - `pillow` >= 12.1.0 - 图片处理
  - `qrcode` >= 8.2 - 二维码生成
- **构建工具**: hatchling
- **包管理器**: uv（推荐）或 pip

---

## 项目结构

```
qrcode49/
├── src/
│   └── qrcode49/
│       ├── __init__.py     # 包初始化文件，定义版本号
│       └── main.py         # 主程序入口，包含所有核心逻辑
├── pyproject.toml          # 项目配置文件（依赖、构建配置、命令入口）
├── .python-version         # Python 版本配置（3.12）
├── .gitignore              # Git 忽略文件配置
├── README.md               # 项目文档
└── AGENTS.md               # 本文件（AI 上下文文档）
```

### 关键文件说明

- **`src/qrcode49/main.py`**: 包含所有核心功能实现，包括：
  - 命令行参数解析
  - 文件类型判断
  - 二维码生成和解析逻辑
  - 输入验证和错误处理
- **`pyproject.toml`**: 项目元数据、依赖管理和构建配置

---

## 构建和运行

### 安装方式

#### 方式一：使用 uv tool 安装（推荐）

```bash
uv tool install qrcode49
```

#### 方式二：使用 pip 安装

```bash
pip install qrcode49
```

#### 方式三：从源码安装（开发模式）

```bash
# 克隆仓库
git clone https://github.com/Nine499/qrcode49.git
cd qrcode49

# 使用 uv 安装
uv pip install -e .

# 或使用 pip 安装
pip install -e .
```

#### 方式四：从本地构建并安装

```bash
# 构建项目
uv build

# 安装构建产物
uv tool install dist/qrcode49-*.whl
```

### 运行命令

#### 生成二维码

```bash
# 默认边长（10）
qrcode49 input.txt output.png

# 自定义边长（20）
qrcode49 input.txt output.png 20

# 使用 Markdown 文件
qrcode49 README.md qrcode.png
```

#### 解析二维码

```bash
# 解析 PNG 图片
qrcode49 input.png output.txt

# 解析 JPG 图片
qrcode49 qrcode.jpg content.txt

# 解析 WebP 图片
qrcode49 qrcode.webp content.txt
```

#### 查看帮助

```bash
qrcode49 --help
```

### 测试命令

当前项目没有配置自动化测试命令。如需添加测试，建议：

1. 在 `pyproject.toml` 中添加测试依赖（如 pytest）
2. 创建 `tests/` 目录
3. 编写测试用例
4. 运行测试：`pytest` 或 `uv run pytest`

---

## 开发约定

### 代码风格

1. **类型注解**: 所有函数参数和返回值都使用类型注解
   ```python
   def generate_qrcode(text: str, output_path: str, box_size: int = 10) -> None:
   ```

2. **文档字符串**: 所有公共函数都包含详细的文档字符串，说明参数和返回值
   ```python
   """
   生成二维码图片

   Args:
       text: 要编码的文本内容
       output_path: 输出图片路径
       box_size: 二维码每个模块的像素大小（边长参数）
   """
   ```

3. **常量定义**: 使用大写命名常量，并添加类型注解
   ```python
   TEXT_EXTENSIONS: set[str] = {'.txt', '.md'}
   IMAGE_EXTENSIONS: set[str] = {'.png', '.jpg', '.jpeg', '.webp'}
   ```

4. **错误处理**: 使用 `try-except` 捕获异常，提供友好的错误信息
   - 使用 `sys.exit(1)` 退出程序
   - 错误信息以 "❌ 错误：" 开头
   - 成功信息以 "✅ " 开头

5. **文件路径处理**: 使用 `pathlib.Path` 进行路径操作
   ```python
   return Path(file_path).suffix.lower() in TEXT_EXTENSIONS
   ```

### 命名约定

- **函数名**: 使用小写字母和下划线（snake_case）
  - `is_text_file()`, `generate_qrcode()`, `decode_qrcode()`
- **变量名**: 使用小写字母和下划线（snake_case）
  - `text_content`, `output_path`, `box_size`
- **常量名**: 使用大写字母和下划线（UPPER_SNAKE_CASE）
  - `TEXT_EXTENSIONS`, `IMAGE_EXTENSIONS`

### 导入顺序

1. 标准库导入
2. 第三方库导入
3. 本地模块导入

```python
import argparse
import os
import sys
from pathlib import Path

import cv2
import qrcode
```

### 版本管理

- 版本号格式：`YYYY.MM.DD.HHMMSS`（基于时间戳）
- 版本号在 `pyproject.toml` 和 `src/qrcode49/__init__.py` 中同步维护
- 使用 `time-version` skill 更新版本号

### Git 提交规范

根据项目历史，提交消息遵循以下格式：

```
<type>(<scope>): <subject>

<type>:
- feat: 新功能
- fix: 修复 bug
- docs: 文档更新
- refactor: 重构代码
- style: 代码格式调整
- test: 测试相关
- chore: 构建/工具相关

<scope>: 可选，标明影响的模块

示例：
- feat(qrcode49): 初始化二维码生成与解析工具项目
- docs: 重写 README 文档，简化内容结构
- refactor: 统一代码结构并更新版本号
```

---

## 依赖管理

### 核心依赖

| 包名 | 版本要求 | 用途 |
|------|----------|------|
| opencv-python | >= 4.12.0.88 | 二维码解析 |
| pillow | >= 12.1.0 | 图片处理 |
| qrcode | >= 8.2 | 二维码生成 |

### 依赖管理工具

- **推荐**: uv（现代、快速的 Python 包管理器）
- **备选**: pip（标准 Python 包管理器）

### 添加新依赖

```bash
# 使用 uv
uv add <package-name>

# 或使用 pip
pip install <package-name>
```

---

## 常见任务

### 添加新功能

1. 在 `src/qrcode49/main.py` 中实现功能
2. 添加类型注解和文档字符串
3. 更新 `README.md` 文档（如需要）
4. 运行测试确保功能正常
5. 提交代码

### 修复 Bug

1. 定位问题代码
2. 修复 bug
3. 验证修复效果
4. 提交代码（使用 `fix` 类型）

### 更新版本号

调用 `time-version` skill 自动更新版本号：

```bash
# 更新版本号（基于当前时间戳）
```

### 发布新版本

1. 更新版本号（使用 `time-version` skill）
2. 更新 `README.md` 中的版本信息（如有变更）
3. 构建项目：
   ```bash
   uv build
   ```
4. 提交代码
5. 推送到远程仓库
6. 发布到 PyPI（如需要）

### 生成文档

使用 `readme-architect` skill 生成或更新文档：

```bash
# 更新 README.md
```

---

## 注意事项

1. **文件编码**: 所有文本文件使用 UTF-8 编码
2. **图片格式**: JPEG 格式需要转换为 RGB 模式（代码已处理）
3. **边长参数**: 推荐范围 1-50，默认值 10
   - 边长越大，二维码图片越大
   - 边长过大可能降低扫描识别度
4. **错误处理**: 所有可能失败的操作都应该有错误处理
5. **用户反馈**: 使用表情符号增强用户体验
   - ✅ 成功
   - ❌ 错误
   - 📄 文本文件
   - 🖼️ 图片文件
   - 📝 内容输出

---

## 技术债务和改进建议

### 当前限制

1. **测试覆盖**: 项目缺少自动化测试
2. **彩色二维码**: 仅支持黑白二维码
3. **批量处理**: 不支持批量生成/解析二维码
4. **配置文件**: 不支持配置文件，所有参数通过命令行传递

### 未来改进方向

1. 添加单元测试和集成测试
2. 支持彩色二维码生成
3. 添加批量处理功能
4. 支持配置文件（如 .qrcode49.toml）
5. 添加更多图片格式支持（如 SVG）
6. 添加二维码美化功能（logo 嵌入、圆角等）

---

## 联系信息

- **GitHub**: https://github.com/Nine499/qrcode49
- **Issues**: https://github.com/Nine499/qrcode49/issues
- **作者**: Nine499

---

## 附录：命令行参数完整说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `input_file` | str | ✅ 是 | - | 输入文件路径（文本文件或图片文件） |
| `output_file` | str | ✅ 是 | - | 输出文件路径 |
| `box_size` | int | ❌ 否 | 10 | 二维码边长（每个模块的像素大小） |

### 支持的文件格式

**输入文件**:
- 文本文件: `.txt`, `.md`
- 图片文件: `.png`, `.jpg`, `.jpeg`, `.webp`

**输出文件**:
- 文本输入 → 图片输出（`.png`, `.jpg`, `.webp`）
- 图片输入 → 文本输出（`.txt`, `.md`）