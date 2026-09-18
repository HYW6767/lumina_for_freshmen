import pathlib

from argparse import ArgumentParser, Namespace
from parse.bootstrap import bootstrap_config
from parse.context import ConfigPath
from parse.path import resolve_paths
from parse.errors import YamlLoadError
from parse.schema.builder import build_schema
from parse.schema.compile import compile_schema
from parse.validation.pipeline import validate_config


def _load_registries():
    from Inference.decoding.registry import DECODING_REGISTRY
    from metrics.registry import METRIC_REGISTRY
    from models.Transformer.losses.registry import LOSS_REGISTRY
    from models.Transformer.modeling.registry import MODEL_REGISTRY
    from models.Transformer.optimizer.registry import OPTIMIZER_REGISTRY
    from models.Transformer.scheduler.registry import SCHEDULER_REGISTRY
    from models.Transformer.tokenizer.registry import TOKENIZER_REGISTRY
    from tasks.registry import TASK_BUILDER_REGISTRY
    from visualize.registry import VISUALIZER_REGISTRY

    return {
        "task": TASK_BUILDER_REGISTRY,
        "tokenizer": TOKENIZER_REGISTRY,
        "model": MODEL_REGISTRY,
        "loss": LOSS_REGISTRY,
        "optimizer": OPTIMIZER_REGISTRY,
        "scheduler": SCHEDULER_REGISTRY,
        "metric": METRIC_REGISTRY,
        "decoding": DECODING_REGISTRY,
        "visualizer": VISUALIZER_REGISTRY,
    }


def _load_spec_registries():
    """加载各动态组件的 ComponentSpec Registry。"""
    from parse.specs.registry import (
        DECODING_SPEC_REGISTRY,
        LOSS_SPEC_REGISTRY,
        METRICS_SPEC_REGISTRY,
        MODEL_SPEC_REGISTRY,
        OPTIMIZER_SPEC_REGISTRY,
        SCHEDULER_SPEC_REGISTRY,
        TASK_SPEC_REGISTRY,
        TOKENIZER_SPEC_REGISTRY,
        VISUALIZER_SPEC_REGISTRY,
    )

    return {
        "task": TASK_SPEC_REGISTRY,
        "tokenizer": TOKENIZER_SPEC_REGISTRY,
        "model": MODEL_SPEC_REGISTRY,
        "loss": LOSS_SPEC_REGISTRY,
        "optimizer": OPTIMIZER_SPEC_REGISTRY,
        "scheduler": SCHEDULER_SPEC_REGISTRY,
        "metric": METRICS_SPEC_REGISTRY,
        "decoding": DECODING_SPEC_REGISTRY,
        "visualizer": VISUALIZER_SPEC_REGISTRY,
    }


def parse_args(argv=None) -> Namespace:
    parser = ArgumentParser(
        description="使用命令行运行 Parse 配置，例如：python start_train.py --config cfg/example.yaml"
    )
    parser.add_argument(
        "--config",
        help="要解析的 YAML 配置路径",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--resume",
        help="训练恢复检查点路径；由外部 Builder 决定是否使用",
        type=str,
        default=None,
    )
    return parser.parse_args(argv)


def load_yaml(config_path):
    config_path = pathlib.Path(config_path).absolute()
    try:
        import yaml
    except ImportError as error:
        raise YamlLoadError("加载YAML配置需要安装PyYAML喵!") from error
    try:
        with config_path.open("r", encoding="utf-8") as config_file:
            raw_config = yaml.safe_load(config_file)
    except (OSError, yaml.YAMLError) as error:
        raise YamlLoadError(f"配置文件: {config_path} 加载失败喵!") from error
    return raw_config, config_path


def parse_config(config_path, expected_mode=None, validate_runtime=False):
    raw_config, config_path = load_yaml(config_path)
    runtime_registries = _load_registries()
    spec_registries = _load_spec_registries()
    context = bootstrap_config(
        raw_config=raw_config,
        config_path=config_path,
        task_registry=runtime_registries["task"],
        task_spec_registry=spec_registries["task"],
        component_registries=runtime_registries,
        component_spec_registries=spec_registries,
        expected_mode=expected_mode,
        validate_runtime=validate_runtime,
    )
    root_schema = build_schema(context, runtime_registries)
    compiled_schema = compile_schema(root_schema)
    normalized_config = compiled_schema.root.normalize(
        value=raw_config,
        path=ConfigPath.root("config"),
        context=context,
    )
    resolved_config = resolve_paths(normalized_config, compiled_schema, context)
    validated_config = validate_config(
        resolved_config,
        context,
        validator_refs=compiled_schema.validator_refs,
    )
    return validated_config, context, compiled_schema

def parse_config_demo(config_path, expected_mode=None, validate_runtime=False):
    return parse_config(
        config_path=config_path,
        expected_mode=expected_mode,
        validate_runtime=validate_runtime,
    )

def normalize_resume_path(resume):
    if resume is None:
        return None
    if not type(resume) in (str, pathlib.Path):
        raise ValueError(f"resume 必须为字符串类型或 pathlib.Path 类型的喵! 现在的type: {type(resume)}")
    if isinstance(resume, str):
        if not resume.strip():
            raise ValueError(f"resume 为字符串类型时不能为空喵!")
    resume_path = pathlib.Path(resume).resolve()
    if not resume_path.exists():
        raise ValueError(F"resume_path: {resume_path} 指向的路径不存在喵!")
    if not resume_path.is_file():
        raise ValueError(f"resume_path: {resume_path} 必须指向文件喵!")
    if resume_path.suffix.casefold() == ".pt":
        return resume_path
    else:
        raise ValueError(f"resume_path: {resume_path} 必须指向pt类型文件喵!")