from typing import Any

from kernelcalls.core.registers import DATA_REGISTER, MODEL_REGISTER


def build_model(name: str, **kwargs: Any) -> Any:
    return MODEL_REGISTER[name](**kwargs)


def build_data(name: str, **kwargs: Any) -> Any:
    return DATA_REGISTER[name](**kwargs)
