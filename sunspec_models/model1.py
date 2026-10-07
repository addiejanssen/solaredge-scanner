from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model1(SunSpecModel):
    """Model definition for SunSpec Model 1 Common"""

    _max_key_length = 11
    _max_description_length = 55

    model_description = {
        "id": "1",
        "name": "common",
        "label": "Common",
        "description": "All SunSpec compliant devices must include this as the first model",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Model identifier", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Model length", ""),
        "mn": (2, 16, ModbusBaseClient.DATATYPE.STRING, str, "", "Well known value registered with SunSpec for compliance", ""),
        "md": (18, 16, ModbusBaseClient.DATATYPE.STRING, str, "", "Manufacturer specific value (32 chars)", ""),
        "opt": (34, 8, ModbusBaseClient.DATATYPE.STRING, str, "", "Manufacturer specific value (16 chars)", ""),
        "vr": (42, 8, ModbusBaseClient.DATATYPE.STRING, str, "", "Manufacturer specific value (16 chars)", ""),
        "sn": (50, 16, ModbusBaseClient.DATATYPE.STRING, str, "", "Manufacturer specific value (32 chars)", ""),
        "da": (66, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Modbus device address", ""),
    }
