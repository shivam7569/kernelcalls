from dataclasses import dataclass, field


@dataclass
class ModelConfig:
    name: str
    kwargs: dict = field(default_factory=dict)


@dataclass
class OptimizerConfig:
    name: str = "AdamW"
    lr: float = 1e-3
    betas: tuple[float, float] = (0.9, 0.999)
    eps: float = 1e-8
    weight_decay: float = 1e-2


@dataclass
class TrainerConfig:
    epochs: int


@dataclass
class DataConfig:
    name: str
    kwargs: dict = field(default_factory=dict)


@dataclass
class SchedulerConfig:
    name: str
    kwargs: dict = field(default_factory=dict)


@dataclass
class ExperimentConfig:
    """
    This config structure class is agnostic to domain. It must remain that way.
    """

    meta: dict
    domain: str
    task: str
    experiment_name: str
    secrets: dict
    seed: int
    callbacks: dict
    model: ModelConfig
    trainer: TrainerConfig
    scheduler: SchedulerConfig
    data: DataConfig
    experiment_dir: str = "."  # Overrides value from local.yaml (if present)
    optimizer: OptimizerConfig = field(default_factory=OptimizerConfig)
