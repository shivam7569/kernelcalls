from collections.abc import Callable

MODEL_REGISTER: dict[str, type] = {}
DATA_REGISTER: dict[str, type] = {}


def register_model(name: str) -> Callable[[type], type]:
    def wrapper(model_class: type) -> type:
        if name in MODEL_REGISTER:
            raise ValueError("Model already registered")
        else:
            MODEL_REGISTER[name] = model_class

        return model_class

    return wrapper


def register_data(name: str) -> Callable[[type], type]:
    def wrapper(data_class: type) -> type:
        if name in DATA_REGISTER:
            raise ValueError("Data already registered")
        else:
            DATA_REGISTER[name] = data_class

        return data_class

    return wrapper
