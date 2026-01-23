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

## 代码风格指南

### 文件结构
- `main.py` - 主程序入口，包含交互式和命令行逻辑
- `core.py` - 核心功能（生成和解码）
- `config.py` - 配置常量

### 命名约定
- **类名**: PascalCase
- **函数名**: snake_case
- **常量**: UPPER_SNAKE_CASE
- **私有函数**: _snake_case

### 类型注解
- 所有函数参数和返回值使用类型注解
- 使用简单类型：int, str, bool, None

### 错误处理
- 使用标准异常：ValueError, FileNotFoundError
- 提供清晰的错误信息
- 在 main.py 中统一捕获异常

### 文档字符串
- 使用中文文档字符串
- 包含 Args、Returns、Raises 部分

### 代码原则
- DRY: 不要重复自己
- YAGNI: 你不需要它
- KISS: 保持简单
- 优先可读性

## 开发注意事项
- 保持代码简洁，避免过度抽象
- 优先使用标准库和核心依赖
- 交互式模式要友好，提供清晰的提示
- 命令行模式要快速，适合脚本使用