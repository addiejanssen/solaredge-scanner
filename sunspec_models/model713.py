from enum import IntEnum

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model713(SunSpecModel):
    """Model definition for SunSpec Model 713 DER Storage Capacity"""

    class Status(IntEnum):
        """States used in this Model"""
    
        OK = 0
        WARNING = 1
        ERROR = 2
    
    _max_key_length = 11
    _max_description_length = 65

    model_description = {
        "id": "713",
        "name": "DERStorageCapacity",
        "label": "DER Storage Capacity",
        "description": "DER storage capacity.",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER storage capacity model ID.", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER storage capacity model length.", ""),
        "whrtg": (2, 1, ModbusBaseClient.DATATYPE.UINT16, int, "wh_sf", "Energy rating of the DER storage.", "WH"),
        "whavail": (3, 1, ModbusBaseClient.DATATYPE.UINT16, int, "wh_sf", "Energy available of the DER storage (WHAvail = WHRtg * SoC * SoH)", "WH"),
        "soc": (4, 1, ModbusBaseClient.DATATYPE.UINT16, int, "pct_sf", "State of charge of the DER storage.", "Pct"),
        "soh": (5, 1, ModbusBaseClient.DATATYPE.UINT16, int, "pct_sf", "State of health of the DER storage.", "Pct"),
        "sta": (6, 1, ModbusBaseClient.DATATYPE.UINT16, Status, "", "Storage status.", ""),
        "wh_sf": (7, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Scale factor for energy capacity.", ""),
        "pct_sf": (8, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Scale factor for percentage.", ""),
    }
