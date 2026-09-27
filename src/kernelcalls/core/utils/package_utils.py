# Utils concerning the operations related to module/package import

import importlib
import pkgutil

from loguru import logger


def import_submodules(package: str) -> list[str]:
    pkg = importlib.import_module(name=package)
    imported_models = []

    for module_info in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        try:
            importlib.import_module(module_info.name)
            if not module_info.ispkg:
                imported_models.append(module_info.name.split(".")[-1])
        except ModuleNotFoundError:
            logger.error(f"Could not find module: {module_info.name}")
            raise ModuleNotFoundError(
                f"{module_info.name} module could not be imported"
            )

    return imported_models
