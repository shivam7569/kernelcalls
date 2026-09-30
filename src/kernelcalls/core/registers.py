from collections.abc import Callable
from typing import Any

from loguru import logger


class Registry:
    def __init__(self, container: str) -> None:
        self.container = container
        setattr(self, container, {})

    def register(self, name: str) -> Callable[[type], type]:
        def wrapper(container_class: type) -> type:
            if name in getattr(self, self.container):
                logger.warning(
                    f"{self.container.capitalize()} {name} is already registered. Continuing, but you may want to verify."
                )
            else:
                getattr(self, self.container)[name] = container_class

            return container_class

        return wrapper

    def get(self, name: str) -> Any:
        if name in getattr(self, self.container):
            return getattr(self, self.container)[name]
        else:
            logger.error(
                f"{self.container.capitalize()} {name} is not available. Please raise an issue on github. Here is the developed {self.container} list: \n{'\n'.join(getattr(self, self.container).keys())}"
            )
            raise ModuleNotFoundError(
                f"{self.container.capitalize()} {name} not available!"
            )

    def build(self, name: str, kwargs: Any = None) -> Any:
        if kwargs is None:
            kwargs = {}
        _class = self.get(name)
        return _class(**kwargs)


MODELS = Registry(container="model")
DATASETS = Registry(container="dataset")
LOSSES = Registry(container="loss")
TASKS = Registry(container="task")
OPTIMIZERS = Registry(container="optimizer")
