# Tiny Tools

A collection of useful utilities and tools for everyday development tasks.

## Installation

```bash
# 创建并激活conda环境
conda create -n tiny-tools python=3.9
conda activate tiny-tools

# 安装项目
pip install -e .
```

## Development Setup

```bash
# 安装开发依赖
pip install -r requirements-dev.txt
```

## Project Structure

```
tiny-tools/
├── src/                    # 源代码目录
│       ├── __init__.py
│       └── core/          # 核心功能模块
├── tests/                 # 测试目录
├── docs/                  # 文档目录
├── examples/             # 示例代码
├── setup.py              # 包安装配置
├── requirements.txt      # 项目依赖
├── requirements-dev.txt  # 开发环境依赖
└── pyproject.toml        # 项目元数据
```

## Development

- 使用 `black` 进行代码格式化
- 使用 `isort` 进行导入排序
- 使用 `flake8` 进行代码检查
- 使用 `mypy` 进行类型检查
- 使用 `pytest` 运行测试

## License

MIT License
