from enum import IntEnum

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model710(SunSpecModel):
    """Model definition for SunSpec Model 710 DER Trip HF"""

    class DerTripHfModuleEnable(IntEnum):
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
        "id": "710",
        "name": "DERTripHF",
        "label": "DER Trip HF",
        "description": "DER high frequency trip model.",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER high frequency trip model ID.", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER high frequency trip model length.", ""),
        "ena": (2, 1, ModbusBaseClient.DATATYPE.UINT16, DerTripHfModuleEnable, "", "DER high frequency trip control enable.", ""),
        "adptcrvreq": (3, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Index of curve points to adopt. First curve index is 1.", ""),
        "adptcrvrslt": (4, 1, ModbusBaseClient.DATATYPE.UINT16, AdoptCurveResult, "", "Result of last adopt curve operation.", ""),
        "npt": (5, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Number of curve points supported.", ""),
        "ncrvset": (6, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Number of stored curves supported.", ""),
        "hz_sf": (7, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Scale factor for curve frequency points.", ""),
        "tms_sf": (8, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Scale factor for curve time points.", ""),
    }
