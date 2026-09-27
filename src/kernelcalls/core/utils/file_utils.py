# Utils concerning the operations related to file deletion/creation/verification

from importlib import resources


def check_config_exists(name: str) -> bool:
    config_file = resources.files(anchor="kernelcalls").joinpath(name)

    return config_file.is_file()
