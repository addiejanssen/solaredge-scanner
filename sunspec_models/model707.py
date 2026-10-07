from enum import IntEnum

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model707(SunSpecModel):
    """Model definition for SunSpec Model 707 DER Trip LV"""

    class DerTripLvModuleEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class AdoptCurveResult(IntEnum):
        """States used in this Model"""
    
        IN_PROGRESS = 0
        COMPLETED = 1
        FAILED = 2
    
    _max_key_length = 11
    _max_description_length = 55

    model_description = {
        "id": "707",
        "name": "DERTripLV",
        "label": "DER Trip LV",
        "description": "DER low voltage trip model.",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER low voltage trip model ID.", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER low voltage trip model length.", ""),
        "ena": (2, 1, ModbusBaseClient.DATATYPE.UINT16, DerTripLvModuleEnable, "", "DER low voltage trip control enable.", ""),
        "adptcrvreq": (3, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Index of curve points to adopt. First curve index is 1.", ""),
        "adptcrvrslt": (4, 1, ModbusBaseClient.DATATYPE.UINT16, AdoptCurveResult, "", "Result of last adopt curve operation.", ""),
        "npt": (5, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Number of curve points supported.", ""),
        "ncrvset": (6, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Number of stored curves supported.", ""),
        "v_sf": (7, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Scale factor for curve voltage points.", ""),
        "tms_sf": (8, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Scale factor for curve time points.", ""),
    }
