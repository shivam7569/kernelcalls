# Utils concerning the operations related to input-output/logging/printing

import json
from typing import Any

from loguru import logger
from omegaconf import DictConfig, ListConfig, OmegaConf


class MetaWrapper(type):
    def __repr__(cls) -> Any:
        if hasattr(cls, "__class_repr__"):
            return cls.__class_repr__()
        else:
            return super().__repr__()


def log_config(cfg: DictConfig | ListConfig) -> None:
    data = OmegaConf.to_container(cfg, resolve=True)

    if isinstance(data, dict):
        secrets = data.get("secrets")
        if isinstance(secrets, dict):
            for key, value in secrets.items():
                if value:
                    secrets[key] = "***"

    formatted = json.dumps(data, indent=2, default=str)
    logger.info(f"Using the following experiment config values: \n{formatted}")


def verify_model_existence(
    imported_models: list[str], config: DictConfig | ListConfig
) -> None:
    if config.model.name in imported_models:
        logger.info(
            f"Imported model {config.model.name} for {config.domain} {config.task} task"
        )
    else:
        logger.error(
            f"Model {config.model.name} is not available. Please raise an issue on github. Here are the developed models: \n{'\n'.join(imported_models)}"
        )
        raise ModuleNotFoundError(f"Model {config.model.name} not available!")
