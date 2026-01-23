# qrcode49 - AI Agent 指南

## 项目概述
简洁友好的二维码生成与解析工具，支持交互式向导和命令行两种模式。

## 环境与工具
- **Python 版本**: 3.12+
- **包管理器**: uv (astral-sh/uv)
- **构建系统**: hatchling
- **核心依赖**: qrcode >=8.0, pillow >=10.0.0, opencv-python-headless >=4.8.0

## 常用命令

### 安装依赖
```bash
uv sync
```

### 运行项目
```bash
# 交互式模式
uv run qrcode49

# 命令行模式
uv run qrcode49 input.txt output.png
uv run qrcode49 input.png output.txt
```

### 构建包
```bash
uv build
```

### 安装为本地包
```bash
uv pip install -e .
```

### 测试
当前项目没有配置自动化测试。手动测试命令：
```bash
# 测试生成
echo "test" > test.txt && uv run qrcode49 test.txt test.png

# 测试解析
uv run qrcode49 test.png test_output.txt && cat test_output.txt

# 清理
rm test.txt test.png test_output.txt
```

## 代码风格指南

### 文件结构
- `main.py` - 主程序入口，包含交互式和命令行逻辑
- `core.py` - 核心功能（生成和解码）
- `config.py` - 配置常量

### 命名约定
- **函数名**: snake_case (如 `generate_qrcode`, `decode_qrcode`)
- **变量名**: snake_case (如 `input_path`, `box_size`)
- **常量**: UPPER_SNAKE_CASE (如 `TEXT_EXTENSIONS`, `DEFAULT_BOX_SIZE`)
- **私有函数**: _snake_case (如 `_helper_function`)

### 类型注解
- 所有函数参数和返回值使用类型注解
- 使用简单类型：int, str, bool, None, list[str]
- 示例：`def generate_qrcode(text: str, output_path: str) -> None:`

### 导入顺序
1. 标准库导入
2. 第三方库导入
3. 本地模块导入

```python
import sys
from pathlib import Path
from qrcode import QRCode, constants
from PIL import Image
from qrcode49.core import generate_qrcode
```

### 文档字符串
- 使用中文文档字符串
- 模块文档：描述模块功能
- 函数文档：包含 Args, Returns, Raises 部分
- 示例：
```python
def generate_qrcode(text: str, output_path: str) -> None:
    """生成二维码图片

    Args:
        text: 要编码的文本内容
        output_path: 输出图片路径

    Raises:
        ValueError: 如果文本为空或参数无效
    """
```

### 错误处理
- 使用标准异常：ValueError, FileNotFoundError
- 提供清晰的错误信息
- 在 main.py 中统一捕获异常
- 使用 try-except 包裹可能失败的操作

### 文件处理
- 使用 `pathlib.Path` 处理路径
- 使用 `with` 语句打开文件
- 指定编码为 utf-8
- 示例：
```python
with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()
```

### 用户输出
- 使用表情符号增强用户体验：✅ ❌ ℹ️ 🎯 📝 🔍
- 成功消息：`print_success(msg)`
- 错误消息：`print_error(msg)` (输出到 stderr)
- 信息消息：`print_info(msg)`

### 代码原则
- **DRY**: 不要重复自己
- **YAGNI**: 你不需要它
- **KISS**: 保持简单
- 优先可读性
- 避免过度抽象

### 退出码
- 0: 成功
- 1: 失败
- 130: 用户中断 (KeyboardInterrupt)

### 交互式模式
- 提供清晰的步骤引导
- 支持默认值（按 Enter 使用）
- 执行前要求用户确认
- 支持取消操作

### 命令行模式
- 自动检测文件类型
- 提供友好的错误提示
- 支持可选参数（如 box_size）

## 开发注意事项
- 保持代码简洁，避免过度抽象
- 优先使用标准库和核心依赖
- 交互式模式要友好，提供清晰的提示
- 命令行模式要快速，适合脚本使用
- 所有文本文件使用 UTF-8 编码
- JPEG 格式需要转换为 RGB 模式