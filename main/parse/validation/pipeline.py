from copy import deepcopy

from parse.errors import ConfigValidationError, RuntimeValidationError


def validate_config(config, context, validator_refs=()):
    if not isinstance(validator_refs, tuple):
        raise TypeError("validator_refs 必须为tuple类型的喵!")
    for validator in sorted(validator_refs, key=lambda item: (item.priority, item.name)):
        if validator.should_run(context, config):
            validator.run(context, config)

    if not isinstance(config, dict):
        raise ConfigValidationError("规范化配置必须为dict类型的喵!")
    if "runtime" not in config or not isinstance(config["runtime"], dict):
        raise ConfigValidationError("规范化配置缺少runtime Mapping喵!")
    if "device" not in config["runtime"] or not isinstance(config["runtime"]["device"], dict):
        raise ConfigValidationError("规范化配置缺少runtime.device Mapping喵!")
    device = config["runtime"]["device"]
    device_type = device["type"]
    device_index = device["index"]
    device_count = device["count"]

    if device_count <= 0:
        raise ConfigValidationError("runtime.device.count 必须为正整数喵!")
    if device_index is not None and device_index < 0:
        raise ConfigValidationError("runtime.device.index 不能为负数喵!")
    if device_type == "cpu" and device_index is not None:
        raise ConfigValidationError("runtime.device.type为cpu时index必须为None喵!")

    if context.validate_runtime and device_type == "cuda":
        try:
            import torch
        except ImportError as error:
            raise RuntimeValidationError("校验CUDA运行环境时无法导入torch喵!") from error
        if not torch.cuda.is_available():
            raise RuntimeValidationError("配置要求CUDA，但当前运行环境没有可用CUDA喵!")
        if device_index is not None and device_index >= torch.cuda.device_count():
            raise RuntimeValidationError(
                f"runtime.device.index: {device_index} 超过CUDA设备数量: {torch.cuda.device_count()} 喵!"
            )
        if device_count > torch.cuda.device_count():
            raise RuntimeValidationError(
                f"runtime.device.count: {device_count} 超过CUDA设备数量: {torch.cuda.device_count()} 喵!"
            )

    return deepcopy(config)
