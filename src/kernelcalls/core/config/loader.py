import subprocess
from importlib import resources
from importlib.abc import Traversable
from pathlib import Path

from omegaconf import DictConfig, ListConfig, OmegaConf

from kernelcalls.core.config.schema import ExperimentConfig


def _traversable_to_str(traversable: Traversable) -> str:
    with resources.as_file(traversable) as path:
        return str(path.resolve())


def _domain_base_config(experiment_yaml: str) -> Traversable:
    domain = Path(experiment_yaml).parts[0]
    domain_base_config_file = resources.files(anchor="kernelcalls").joinpath(
        f"{domain}/configs/base.yaml"
    )

    return domain_base_config_file


def _get_git_commit_info(short: bool = False) -> dict[str, str]:
    repo_root = Path(__file__).resolve().parents[4]
    hash_cmd = ["git", "rev-parse"]
    branch_cmd = ["git", "rev-parse", "--abbrev-ref"]
    if short:
        hash_cmd.append("--short")

    hash_cmd.append("HEAD")
    branch_cmd.append("HEAD")

    try:
        commit_hash = subprocess.check_output(
            hash_cmd, cwd=repo_root, text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        commit_hash = "unknown"

    try:
        branch_name = subprocess.check_output(
            branch_cmd, cwd=repo_root, text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        branch_name = "unknown"

    return {"commit_hash": commit_hash, "branch_name": branch_name}


def load_config(
    experiment_yaml: str,
    schema: type = ExperimentConfig,
    overrides: list[str] | None = None,
) -> DictConfig | ListConfig:
    core_base_config_path = resources.files(anchor="kernelcalls").joinpath(
        "configs/base.yaml"
    )
    domain_base_config_path = _domain_base_config(experiment_yaml=experiment_yaml)
    experiment_yaml_path = resources.files(anchor="kernelcalls").joinpath(
        experiment_yaml
    )
    local_config_path = resources.files(anchor="kernelcalls").joinpath(
        "configs/local.yaml"
    )

    layers = [
        OmegaConf.structured(schema),  # The structure of the config
        OmegaConf.load(
            _traversable_to_str(core_base_config_path)
        ),  # First, the core base config values
        OmegaConf.load(
            _traversable_to_str(domain_base_config_path)
        ),  # Second, the domain specific config values
        OmegaConf.load(
            _traversable_to_str(experiment_yaml_path)
        ),  # Third, the experiment config values
    ]

    if local_config_path.is_file():
        layers.append(OmegaConf.load(_traversable_to_str(local_config_path)))

    config = OmegaConf.merge(*layers)
    config = OmegaConf.merge(config, OmegaConf.from_dotlist(overrides or []))
    config.meta = _get_git_commit_info()
    OmegaConf.resolve(config)
    OmegaConf.set_readonly(config, value=True)

    return config
