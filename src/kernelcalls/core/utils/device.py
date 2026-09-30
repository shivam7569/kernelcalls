import torch
from loguru import logger


def get_compute_device(device: str) -> tuple[str, str]:

    if device not in (allowed_values := ["auto", "cpu", "cuda"]):
        logger.error(
            f"Device {device} is not supported. Allowed values are: \n{'\n'.join(allowed_values)}"
        )
        raise ValueError(f"Invalid device value input: {device}")

    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"

    device_name = torch.cuda.get_device_name() if device == "cuda" else "cpu"

    return (device, device_name)
