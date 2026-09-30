from torch import nn

from kernelcalls.core.registers import LOSSES

LOSSES.register(name="cross_entropy")(nn.CrossEntropyLoss)
