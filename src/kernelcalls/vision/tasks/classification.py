from typing import Any

from torch import Tensor, nn

from kernelcalls.core.contracts import VisionClassificationLoss
from kernelcalls.core.registers import LOSSES, TASKS

DEFAULT_CLASSIFICATION_LOSS = LOSSES.build(name="cross_entropy")


@TASKS.register(name="classification")
class ClassificationTask(nn.Module):
    def __init__(
        self,
        network: nn.Module,
        loss: VisionClassificationLoss,
        kwargs: Any = None,
    ) -> None:
        super().__init__()

        self.network = network
        self.loss = loss if loss is not None else DEFAULT_CLASSIFICATION_LOSS
        self.kwargs = kwargs

    def training_step(self, batch: tuple[Tensor, Tensor]) -> Tensor:
        images, labels = batch
        logits = self.network(images)
        loss = self.loss(logits, labels)

        return loss

    def validation_step(self, batch: tuple[Tensor, Tensor]) -> float:
        images, labels = batch
        logits = self.network(images)
        loss = self.loss(logits, labels)

        return loss.item()
