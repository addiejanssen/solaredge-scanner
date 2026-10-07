from enum import IntEnum

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model712(SunSpecModel):
    """Model definition for SunSpec Model 712 DER Watt-Var"""

    class DerWattVarModuleEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class SetActiveCurveResult(IntEnum):
        """States used in this Model"""
    
        IN_PROGRESS = 0
        COMPLETED = 1
        FAILED = 2
    
    _max_key_length = 11
    _max_description_length = 50

    model_description = {
        "id": "712",
        "name": "DERWattVar",
        "label": "DER Watt-Var",
        "description": "DER Watt-Var model.",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER Watt-Var model ID.", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER Watt-Var model length.", ""),
        "ena": (2, 1, ModbusBaseClient.DATATYPE.UINT16, DerWattVarModuleEnable, "", "DER Watt-Var control enable.", ""),
        "adptcrvreq": (3, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Set active curve. 0 = No active curve.", ""),
        "adptcrvrslt": (4, 1, ModbusBaseClient.DATATYPE.UINT16, SetActiveCurveResult, "", "Result of last set active curve operation.", ""),
        "npt": (5, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Number of curve points supported.", ""),
        "ncrv": (6, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Number of stored curves supported.", ""),
        "rvrttms": (7, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Reversion time in seconds.  0 = No reversion time.", "Secs"),
        "rvrtrem": (9, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Reversion time remaining in seconds.", "Secs"),
        "rvrtcrv": (11, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Default curve after reversion timeout.", ""),
        "w_sf": (12, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Scale factor for curve active power points.", ""),
        "deptref_sf": (13, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Scale factor for curve var points.", ""),
    }
