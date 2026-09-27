import os
import sys

from loguru import logger


def setup_logger(
    experiment_dir: str, experiment_name: str, verbose: bool = True
) -> None:
    logger.remove()
    level = "DEBUG" if verbose else "INFO"
    log_format = "<green>{time:HH:mm:ss}</green> - <magenta>{extra[experiment_name]}</magenta> | <level>{level: <4}</level> | <cyan>{name}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    logger.add(
        sink=sys.stderr,
        format=log_format,
        level=level,
    )

    logger.configure(extra={"experiment_name": experiment_name})

    logger.add(
        sink=os.path.join(experiment_dir, "experiment.log"),
        format=log_format,
        level=level,
    )
