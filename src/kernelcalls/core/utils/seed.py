import random

import numpy as np
import torch


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def seed_dataloader_worker(worker_id: int) -> None:
    worker_seed = (
        torch.initial_seed() % (2**32)
    )  # % (2**32) is required because numpy.random.seed() only accepts an unsigned 32-bit integer
    # (a value between $0$ and $2^{32} - 1$), whereas torch.initial_seed() returns a 64-bit integer.
    np.random.seed(worker_seed)
    random.seed(worker_seed)


def seed_dataloader_generator(seed: int) -> torch.Generator:
    generator = torch.Generator()
    generator.manual_seed(seed)

    return generator
