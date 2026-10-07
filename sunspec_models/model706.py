from enum import IntEnum

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model706(SunSpecModel):
    """Model definition for SunSpec Model 706 DER Volt-Watt"""

    class DerVoltWattModuleEnable(IntEnum):
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
        "id": "706",
        "name": "DERVoltWatt",
        "label": "DER Volt-Watt",
        "description": "DER Volt-Watt model.",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER Volt-Watt model ID.", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER Volt-Watt model length.", ""),
        "ena": (2, 1, ModbusBaseClient.DATATYPE.UINT16, DerVoltWattModuleEnable, "", "Volt-Watt control enable.", ""),
        "adptcrvreq": (3, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Index of curve points to adopt. First curve index is 1.", ""),
        "adptcrvrslt": (4, 1, ModbusBaseClient.DATATYPE.UINT16, AdoptCurveResult, "", "Result of last adopt curve operation.", ""),
        "npt": (5, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Number of curve points supported.", ""),
        "ncrv": (6, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Number of stored curves supported.", ""),
        "rvrttms": (7, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Reversion time in seconds.  0 = No reversion time.", "Secs"),
        "rvrtrem": (9, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Reversion time remaining in seconds.", "Secs"),
        "rvrtcrv": (11, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Default curve after reversion timeout.", ""),
        "v_sf": (12, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Scale factor for curve voltage points.", ""),
        "deptref_sf": (13, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Scale factor for curve watt points.", ""),
        "rsptms_sf": (14, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Open loop response time scale factor.", ""),
    }
