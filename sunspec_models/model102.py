from enum import IntEnum, IntFlag

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model102(SunSpecModel):
    """Model definition for SunSpec Model 102 Inverter (Split-Phase)"""

    class OperatingState(IntEnum):
        """States used in this Model"""
    
        OFF = 1
        SLEEPING = 2
        STARTING = 3
        MPPT = 4
        THROTTLED = 5
        SHUTTING_DOWN = 6
        FAULT = 7
        STANDBY = 8
    
    class Event1(IntFlag):
        """Flags used in this Model"""
    
        GROUND_FAULT = 0
        DC_OVER_VOLT = 1
        AC_DISCONNECT = 2
        DC_DISCONNECT = 3
        GRID_DISCONNECT = 4
        CABINET_OPEN = 5
        MANUAL_SHUTDOWN = 6
        OVER_TEMP = 7
        OVER_FREQUENCY = 8
        UNDER_FREQUENCY = 9
        AC_OVER_VOLT = 10
        AC_UNDER_VOLT = 11
        BLOWN_STRING_FUSE = 12
        UNDER_TEMP = 13
        MEMORY_LOSS = 14
        HW_TEST_FAILURE = 15
    
    _max_key_length = 11
    _max_description_length = 36

    model_description = {
        "id": "102",
        "name": "inverter_split_phase",
        "label": "Inverter (Split-Phase)",
        "description": "Include this model for split phase inverter monitoring",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Model identifier", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Model length", ""),
        "a": (2, 1, ModbusBaseClient.DATATYPE.UINT16, int, "a_sf", "AC Current", "A"),
        "apha": (3, 1, ModbusBaseClient.DATATYPE.UINT16, int, "a_sf", "Phase A Current", "A"),
        "aphb": (4, 1, ModbusBaseClient.DATATYPE.UINT16, int, "a_sf", "Phase B Current", "A"),
        "aphc": (5, 1, ModbusBaseClient.DATATYPE.UINT16, int, "a_sf", "Phase C Current", "A"),
        "a_sf": (6, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "ppvphab": (7, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase Voltage AB", "V"),
        "ppvphbc": (8, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase Voltage BC", "V"),
        "ppvphca": (9, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase Voltage CA", "V"),
        "phvpha": (10, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase Voltage AN", "V"),
        "phvphb": (11, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase Voltage BN", "V"),
        "phvphc": (12, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase Voltage CN", "V"),
        "v_sf": (13, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "w": (14, 1, ModbusBaseClient.DATATYPE.INT16, int, "w_sf", "AC Power", "W"),
        "w_sf": (15, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "hz": (16, 1, ModbusBaseClient.DATATYPE.UINT16, int, "hz_sf", "Line Frequency", "Hz"),
        "hz_sf": (17, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "va": (18, 1, ModbusBaseClient.DATATYPE.INT16, int, "va_sf", "AC Apparent Power", "VA"),
        "va_sf": (19, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "var": (20, 1, ModbusBaseClient.DATATYPE.INT16, int, "var_sf", "AC Reactive Power", "var"),
        "var_sf": (21, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "pf": (22, 1, ModbusBaseClient.DATATYPE.INT16, int, "pf_sf", "AC Power Factor", "Pct"),
        "pf_sf": (23, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "wh": (24, 2, ModbusBaseClient.DATATYPE.UINT32, int, "wh_sf", "AC Energy", "Wh"),
        "wh_sf": (26, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "dca": (27, 1, ModbusBaseClient.DATATYPE.UINT16, int, "dca_sf", "DC Current", "A"),
        "dca_sf": (28, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "dcv": (29, 1, ModbusBaseClient.DATATYPE.UINT16, int, "dcv_sf", "DC Voltage", "V"),
        "dcv_sf": (30, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "dcw": (31, 1, ModbusBaseClient.DATATYPE.INT16, int, "dcw_sf", "DC Power", "W"),
        "dcw_sf": (32, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "tmpcab": (33, 1, ModbusBaseClient.DATATYPE.INT16, int, "tmp_sf", "Cabinet Temperature", "C"),
        "tmpsnk": (34, 1, ModbusBaseClient.DATATYPE.INT16, int, "tmp_sf", "Heat Sink Temperature", "C"),
        "tmptrns": (35, 1, ModbusBaseClient.DATATYPE.INT16, int, "tmp_sf", "Transformer Temperature", "C"),
        "tmpot": (36, 1, ModbusBaseClient.DATATYPE.INT16, int, "tmp_sf", "Other Temperature", "C"),
        "tmp_sf": (37, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "", ""),
        "st": (38, 1, ModbusBaseClient.DATATYPE.UINT16, OperatingState, "", "Enumerated value.  Operating state", ""),
        "stvnd": (39, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Vendor specific operating state code", ""),
        "evt1": (40, 2, ModbusBaseClient.DATATYPE.UINT32, Event1, "", "Bitmask value. Event fields", ""),
        "evt2": (42, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Reserved for future use", ""),
        "evtvnd1": (44, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Vendor defined events", ""),
        "evtvnd2": (46, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Vendor defined events", ""),
        "evtvnd3": (48, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Vendor defined events", ""),
        "evtvnd4": (50, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Vendor defined events", ""),
    }
