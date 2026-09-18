from copy import deepcopy
from collections.abc import Mapping
from pathlib import Path

from parse.context import MISSING
from parse.errors import PathResolutionError


def _resolve_path_values(value, base_path):
    if isinstance(value, Path):
        if value.is_absolute():
            return value.resolve()
        return (base_path / value).resolve()
    if isinstance(value, dict):
        return {
            key: _resolve_path_values(child_value, base_path)
            for key, child_value in value.items()
        }
    if isinstance(value, list):
        return [_resolve_path_values(child_value, base_path) for child_value in value]
    if isinstance(value, tuple):
        return tuple(_resolve_path_values(child_value, base_path) for child_value in value)
    return value


def resolve_paths(config, compiled_schema, context):
    if not isinstance(config, dict):
        raise PathResolutionError("待解析配置必须为dict类型的喵!")
    result = deepcopy(config)
    data_config = result.get("data")
    dataset_config = data_config.get("dataset") if isinstance(data_config, dict) else None
    original_splits = (
        deepcopy(dataset_config.get("splits"))
        if isinstance(dataset_config, dict)
        else None
    )
    result = _resolve_path_values(result, context.config_dir)
    if isinstance(original_splits, dict):
        resolved_dataset = result["data"]["dataset"]
        dataset_root = resolved_dataset.get("root")
        if isinstance(dataset_root, Path):
            for split_name, split_path in original_splits.items():
                split_path = Path(split_path)
                if split_path.is_absolute():
                    resolved_dataset["splits"][split_name] = split_path.resolve()
                else:
                    resolved_dataset["splits"][split_name] = (
                        dataset_root / split_path
                    ).resolve()
    return result
