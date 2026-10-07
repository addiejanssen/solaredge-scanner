__all__: list[str] = [
    "Model1",
    "Model101",
    "Model102",
    "Model103",
    "Model201",
    "Model202",
    "Model203",
    "Model204",
    "Model701",
    "Model702",
    "Model703",
    "Model704",
    "Model705",
    "Model706",
    "Model707",
    "Model708",
    "Model709",
    "Model710",
    "Model711",
    "Model712",
    "Model713",
    "SunSpecNotImplemented",
]

from typing import LiteralString

from .model1 import Model1
from .model101 import Model101
from .model102 import Model102
from .model103 import Model103
from .model201 import Model201
from .model202 import Model202
from .model203 import Model203
from .model204 import Model204
from .model701 import Model701
from .model702 import Model702
from .model703 import Model703
from .model704 import Model704
from .model705 import Model705
from .model706 import Model706
from .model707 import Model707
from .model708 import Model708
from .model709 import Model709
from .model710 import Model710
from .model711 import Model711
from .model712 import Model712
from .model713 import Model713
from .sunspec import SunSpecModel, SunSpecNotImplemented

__version__: str = "0.0.1"
__version_full__: str = f"[solaredge, version {__version__}]"

_all_models: dict[int, type] = {
    1: Model1,
    101: Model101,
    102: Model102,
    103: Model103,
    203: Model203,
    701: Model701,
    702: Model702,
    703: Model703,
    704: Model704,
    705: Model705,
    706: Model706,
    707: Model707,
    708: Model708,
    709: Model709,
    710: Model710,
    711: Model711,
    712: Model712,
    713: Model713,
}


def get_model(registers: list[int]) -> type:
    """Return the Model class that matches the model id in the supplied registers"""
    id = SunSpecModel.find_model_id(registers)
    return _all_models[id]
