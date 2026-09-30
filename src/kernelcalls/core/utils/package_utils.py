# Utils concerning the operations related to module/package import

import importlib
import pkgutil

from loguru import logger


def import_submodules(package: str | list[str]) -> None:
    if isinstance(package, list):
        for _pkg in package:
            import_submodules(_pkg)
    elif isinstance(package, str):
        pkg = importlib.import_module(name=package)
        for module_info in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
            try:
                importlib.import_module(module_info.name)
            except ModuleNotFoundError:
                logger.error(f"Could not find module: {module_info.name}")
                raise ModuleNotFoundError(
                    f"{module_info.name} module could not be imported"
                )
