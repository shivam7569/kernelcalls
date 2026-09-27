# Utils concerning the operations related to input-output/logging/printing

import json

from loguru import logger
from omegaconf import DictConfig, ListConfig, OmegaConf


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
