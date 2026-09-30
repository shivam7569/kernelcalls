from torch import optim

from kernelcalls.core.registers import OPTIMIZERS

OPTIMIZERS.register(name="adam")(optim.Adam)
OPTIMIZERS.register(name="sgd")(optim.SGD)
OPTIMIZERS.register(name="adamW")(optim.AdamW)
OPTIMIZERS.register(name="rmsprop")(optim.RMSprop)
OPTIMIZERS.register(name="adagrad")(optim.Adagrad)
OPTIMIZERS.register(name="adadelta")(optim.Adadelta)
