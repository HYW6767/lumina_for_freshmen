"""检查项目运行所需的 Python、依赖和 CUDA 环境。"""

from __future__ import annotations

import importlib
import importlib.metadata
import os
import platform
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
REQUIREMENTS_FILE = PROJECT_ROOT / "requirements.txt"

IMPORT_NAMES = {
    "PyYAML": "yaml",
}

EXPECTED_PYTHON = "3.11.14"


def base_version(version: str) -> str:
    return version.split("+")[0].strip()


def get_env_info() -> str:
    conda_env = os.environ.get("CONDA_DEFAULT_ENV")
    conda_prefix = os.environ.get("CONDA_PREFIX")
    venv = os.environ.get("VIRTUAL_ENV")
    if conda_env or conda_prefix:
        return f"Conda 环境 {conda_env or ''} ({conda_prefix or sys.prefix})".strip()
    if venv:
        return f"venv/virtualenv ({venv})"
    if sys.prefix != getattr(sys, "base_prefix", sys.prefix):
        return f"虚拟环境 ({sys.prefix})"
    return f"系统 Python ({sys.prefix})"


def read_requirements() -> list[tuple[str, str | None]]:
    requirements: list[tuple[str, str | None]] = []
    requirement_pattern = re.compile(r"^([A-Za-z0-9_.-]+)\s*(?:==\s*([^;#\s]+))?")

    if not REQUIREMENTS_FILE.exists():
        return requirements

    for raw_line in REQUIREMENTS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        match = requirement_pattern.match(line)
        if match:
            requirements.append((match.group(1), match.group(2)))
    return requirements


def check_dependency(package_name: str, expected_version: str | None) -> str:
    module_name = IMPORT_NAMES.get(package_name, package_name)
    try:
        module = importlib.import_module(module_name)
        installed_version = importlib.metadata.version(package_name)
    except (ImportError, importlib.metadata.PackageNotFoundError) as error:
        return f"失败: {package_name} 未安装或无法导入 ({error})"

    version_result = f"版本 {installed_version}"
    module_version = getattr(module, "__version__", None)

    # torch 的 metadata 显示 2.9.1，但 torch.__version__ 可能报告 2.9.1+cu128。
    # 以去掉本地构建后缀后的版本号比较为准，避免在你的环境上误报。
    checked_version = base_version(module_version) if module_version else installed_version
    if expected_version and checked_version != expected_version:
        version_result += f"，要求 {expected_version}"
        return f"警告: {package_name} {version_result}"

    if module_version and base_version(module_version) != base_version(installed_version):
        version_result += f"，模块报告 {module_version}"
        return f"警告: {package_name} ({version_result})"
    if module_version and module_version != installed_version:
        version_result += f"，模块报告 {module_version}"
    return f"通过: {package_name} ({version_result})"


def print_runtime_info() -> None:
    python_version = platform.python_version()
    print("=== NLP 环境自查 ===")
    print(f"Python 版本: {python_version}")
    if python_version == EXPECTED_PYTHON:
        print(f"Python 版本检查: 通过（要求 {EXPECTED_PYTHON}）")
    else:
        print(f"Python 版本检查: 警告（当前 {python_version}，要求 {EXPECTED_PYTHON}）")
    print(f"Python 可执行文件: {sys.executable}")
    print(f"操作系统: {platform.platform()}")
    print(f"系统架构: {platform.machine()}")
    print(f"处理器: {platform.processor() or '未知'}")
    print(f"当前目录: {Path.cwd()}")
    print(f"虚拟环境: {get_env_info()}")
    print(f"requirements.txt: {REQUIREMENTS_FILE}")


def print_torch_info() -> None:
    try:
        import torch
    except ImportError as error:
        print(f"PyTorch 运行检查失败: {error}")
        return

    print(f"PyTorch 编译版本: {torch.__version__}")
    print(f"PyTorch CUDA runtime: {torch.version.cuda or '无 CUDA runtime'}")
    print(f"CUDA 可用: {torch.cuda.is_available()}")

    if not torch.cuda.is_available():
        print("GPU 数量: 0")
        print("CUDA 测试: 跳过（当前环境未检测到可用 CUDA）")
        return

    device_count = torch.cuda.device_count()
    print(f"GPU 数量: {device_count}")
    for index in range(device_count):
        properties = torch.cuda.get_device_properties(index)
        memory_gib = properties.total_memory / 1024**3
        capability = f"{properties.major}.{properties.minor}"
        print(
            f"GPU {index}: {properties.name} | 显存 {memory_gib:.1f} GiB "
            f"| Compute Capability {capability}"
        )

    try:
        left = torch.randn(512, 512, device="cuda")
        right = torch.randn(512, 512, device="cuda")
        result = left @ right
        torch.cuda.synchronize()
        print(f"CUDA 计算测试: 通过（{result.device}，结果形状 {tuple(result.shape)}）")
    except (RuntimeError, AssertionError) as error:
        print(f"CUDA 计算测试: 失败（{error}）")


def main() -> None:
    print_runtime_info()
    print("\n=== requirements.txt 依赖检查 ===")
    requirements = read_requirements()
    if not requirements:
        print(f"警告: 未找到有效依赖配置: {REQUIREMENTS_FILE}")
    else:
        for package_name, expected_version in requirements:
            print(check_dependency(package_name, expected_version))
    print("\n=== PyTorch 设备检查 ===")
    print_torch_info()


if __name__ == "__main__":
    main()
