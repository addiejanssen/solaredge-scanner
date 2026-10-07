from enum import IntEnum

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model711(SunSpecModel):
    """Model definition for SunSpec Model 711 DER Frequency Droop"""

    class DerFrequencyDroopModuleEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class SetActiveControlResult(IntEnum):
        """States used in this Model"""
    
        IN_PROGRESS = 0
        COMPLETED = 1
        FAILED = 2
    
    _max_key_length = 11
    _max_description_length = 52

    model_description = {
        "id": "711",
        "name": "DERFreqDroop",
        "label": "DER Frequency Droop",
        "description": "DER Frequency Droop model.",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER Frequency Droop model ID.", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER Frequency Droop model length.", ""),
        "ena": (2, 1, ModbusBaseClient.DATATYPE.UINT16, DerFrequencyDroopModuleEnable, "", "DER Frequency-Watt (Frequency-Droop) control enable.", ""),
        "adptctlreq": (3, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Set active control. 0 = No active control.", ""),
        "adptctlrslt": (4, 1, ModbusBaseClient.DATATYPE.UINT16, SetActiveControlResult, "", "Result of last set active control operation.", ""),
        "nctl": (5, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Number of stored controls supported.", ""),
        "rvrttms": (6, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Reversion time in seconds.  0 = No reversion time.", "Secs"),
        "rvrtrem": (8, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Reversion time remaining in seconds.", "Secs"),
        "rvrtctl": (10, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Default control after reversion timeout.", ""),
        "db_sf": (11, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Deadband scale factor.", ""),
        "k_sf": (12, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Frequency change scale factor.", ""),
        "rsptms_sf": (13, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Open loop response time scale factor.", ""),
    }
