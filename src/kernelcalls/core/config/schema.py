from dataclasses import dataclass, field


@dataclass
class ModelConfig:
    name: str
    kwargs: dict = field(default_factory=dict)


@dataclass
class OptimizerConfig:
    name: str
    kwargs: dict = field(default_factory=dict)


@dataclass
class TrainerConfig:
    epochs: int = 1  # to test the pipeline
    device: str = "auto"


@dataclass
class DataConfig:
    name: str
    kwargs: dict = field(default_factory=dict)


@dataclass
class SchedulerConfig:
    name: str
    kwargs: dict = field(default_factory=dict)


@dataclass
class TaskConfig:
    name: str
    kwargs: dict = field(default_factory=dict)


@dataclass
class LossConfig:
    name: str
    kwargs: dict = field(default_factory=dict)


@dataclass
class ExperimentConfig:
    """
    This config structure class is agnostic to domain. It must remain that way.
    """

    meta: dict
    domain: str
    experiment_name: str
    secrets: dict
    seed: int
    callbacks: dict
    model: ModelConfig
    scheduler: SchedulerConfig
    data: DataConfig
    task: TaskConfig
    optimizer: OptimizerConfig
    trainer: TrainerConfig = field(default_factory=TrainerConfig)
    loss: LossConfig | None = None
    experiment_dir: str = "."  # Overrides value from local.yaml (if present)
