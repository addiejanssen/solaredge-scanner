from enum import IntEnum

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model703(SunSpecModel):
    """Model definition for SunSpec Model 703 Enter Service"""

    class PermitEnterService(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    _max_key_length = 11
    _max_description_length = 66

    model_description = {
        "id": "703",
        "name": "DEREnterService",
        "label": "Enter Service",
        "description": "Enter service model.",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Enter service model ID.", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Enter service model length.", ""),
        "es": (2, 1, ModbusBaseClient.DATATYPE.UINT16, PermitEnterService, "", "Permit enter service.", ""),
        "esvhi": (3, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Enter service voltage high threshold as percent of normal voltage.", "Pct"),
        "esvlo": (4, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Enter service voltage low threshold as percent of normal voltage.", "Pct"),
        "eshzhi": (5, 2, ModbusBaseClient.DATATYPE.UINT32, int, "hz_sf", "Enter service frequency high threshold.", "Hz"),
        "eshzlo": (7, 2, ModbusBaseClient.DATATYPE.UINT32, int, "hz_sf", "Enter service frequency low threshold.", "Hz"),
        "esdlytms": (9, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Enter service delay time in seconds.", "Secs"),
        "esrndtms": (11, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Enter service random delay in seconds.", "Secs"),
        "esrmptms": (13, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Enter service ramp time in seconds.", "Secs"),
        "esdlyremtms": (15, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Enter service delay time remaining in seconds.", "Secs"),
        "v_sf": (17, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Voltage percentage scale factor.", ""),
        "hz_sf": (18, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Frequency scale factor.", ""),
    }
