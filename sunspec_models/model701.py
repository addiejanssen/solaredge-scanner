from enum import IntEnum, IntFlag

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model701(SunSpecModel):
    """Model definition for SunSpec Model 701 DER AC Measurement"""

    class AcWiringType(IntEnum):
        """States used in this Model"""
    
        SINGLE_PHASE = 0
        SPLIT_PHASE = 1
        THREE_PHASE = 2
    
    class OperatingState(IntEnum):
        """States used in this Model"""
    
        OFF = 0
        ON = 1
    
    class InverterState(IntEnum):
        """States used in this Model"""
    
        OFF = 0
        SLEEPING = 1
        STARTING = 2
        RUNNING = 3
        THROTTLED = 4
        SHUTTING_DOWN = 5
        FAULT = 6
        STANDBY = 7
    
    class GridConnectionState(IntEnum):
        """States used in this Model"""
    
        DISCONNECTED = 0
        CONNECTED = 1
    
    class AlarmBitfield(IntFlag):
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
        MANUFACTURER_ALRM = 16
    
    class DerOperationalCharacteristics(IntFlag):
        """Flags used in this Model"""
    
        GRID_FOLLOWING = 0
        GRID_FORMING = 1
        PV_CLIPPED = 2
    
    class ThrottleSourceInformation(IntFlag):
        """Flags used in this Model"""
    
        MAX_W = 0
        FIXED_W = 1
        FIXED_VAR = 2
        FIXED_PF = 3
        VOLT_VAR = 4
        FREQ_WATT = 5
        DYN_REACT_CURR = 6
        LVRT = 7
        HVRT = 8
        WATT_VAR = 9
        VOLT_WATT = 10
        SCHEDULED = 11
        LFRT = 12
        HFRT = 13
        DERATED = 14
    
    _max_key_length = 12
    _max_description_length = 92

    model_description = {
        "id": "701",
        "name": "DERMeasureAC",
        "label": "DER AC Measurement",
        "description": "DER AC measurement model.",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER AC measurement model ID.", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER AC measurement model length.", ""),
        "actype": (2, 1, ModbusBaseClient.DATATYPE.UINT16, AcWiringType, "", "AC wiring type.", ""),
        "st": (3, 1, ModbusBaseClient.DATATYPE.UINT16, OperatingState, "", "Operating state of the DER.", ""),
        "invst": (4, 1, ModbusBaseClient.DATATYPE.UINT16, InverterState, "", "Enumerated value.  Inverter state.", ""),
        "connst": (5, 1, ModbusBaseClient.DATATYPE.UINT16, GridConnectionState, "", "Grid connection state of the DER.", ""),
        "alrm": (6, 2, ModbusBaseClient.DATATYPE.UINT32, AlarmBitfield, "", "Active alarms for the DER.", ""),
        "dermode": (8, 2, ModbusBaseClient.DATATYPE.UINT32, DerOperationalCharacteristics, "", "Current operational characteristics of the DER.", ""),
        "w": (10, 1, ModbusBaseClient.DATATYPE.INT16, int, "w_sf", "Total active power. Active power is positive for DER generation and negative for absorption.", "W"),
        "va": (11, 1, ModbusBaseClient.DATATYPE.INT16, int, "va_sf", "Total apparent power.", "VA"),
        "var": (12, 1, ModbusBaseClient.DATATYPE.INT16, int, "var_sf", "Total reactive power.", "Var"),
        "pf": (13, 1, ModbusBaseClient.DATATYPE.INT16, int, "pf_sf", "Power factor. The sign of power factor should be the sign of active power.", ""),
        "a": (14, 1, ModbusBaseClient.DATATYPE.INT16, int, "a_sf", "Total AC current.", "A"),
        "llv": (15, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Line to line AC voltage as an average of active phases.", "V"),
        "lnv": (16, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Line to neutral AC voltage as an average of active phases.", "V"),
        "hz": (17, 2, ModbusBaseClient.DATATYPE.UINT32, int, "hz_sf", "AC frequency.", "Hz"),
        "totwhinj": (19, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totwh_sf", "Total active energy injected (Quadrants 1 & 4).", "Wh"),
        "totwhabs": (23, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totwh_sf", "Total active energy absorbed (Quadrants 2 & 3).", "Wh"),
        "totvarhinj": (27, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totvarh_sf", "Total reactive energy injected (Quadrants 1 & 2).", "Varh"),
        "totvarhabs": (31, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totvarh_sf", "Total reactive energy absorbed (Quadrants 3 & 4).", "Varh"),
        "tmpamb": (35, 1, ModbusBaseClient.DATATYPE.INT16, int, "tmp_sf", "Ambient temperature.", "C"),
        "tmpcab": (36, 1, ModbusBaseClient.DATATYPE.INT16, int, "tmp_sf", "Cabinet temperature.", "C"),
        "tmpsnk": (37, 1, ModbusBaseClient.DATATYPE.INT16, int, "tmp_sf", "Heat sink temperature.", "C"),
        "tmptrns": (38, 1, ModbusBaseClient.DATATYPE.INT16, int, "tmp_sf", "Transformer temperature.", "C"),
        "tmpsw": (39, 1, ModbusBaseClient.DATATYPE.INT16, int, "tmp_sf", "IGBT/MOSFET temperature.", "C"),
        "tmpot": (40, 1, ModbusBaseClient.DATATYPE.INT16, int, "tmp_sf", "Other temperature.", "C"),
        "wl1": (41, 1, ModbusBaseClient.DATATYPE.INT16, int, "w_sf", "Active power L1.", "W"),
        "val1": (42, 1, ModbusBaseClient.DATATYPE.INT16, int, "va_sf", "Apparent power L1.", "VA"),
        "varl1": (43, 1, ModbusBaseClient.DATATYPE.INT16, int, "var_sf", "Reactive power L1.", "Var"),
        "pfl1": (44, 1, ModbusBaseClient.DATATYPE.INT16, int, "pf_sf", "Power factor phase L1.", ""),
        "al1": (45, 1, ModbusBaseClient.DATATYPE.INT16, int, "a_sf", "Current phase L1.", "A"),
        "vl1l2": (46, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase voltage L1-L2.", "V"),
        "vl1": (47, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase voltage L1-N.", "V"),
        "totwhinjl1": (48, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totwh_sf", "Total active energy injected L1.", "Wh"),
        "totwhabsl1": (52, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totwh_sf", "Total active energy absorbed L1.", "Wh"),
        "totvarhinjl1": (56, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totvarh_sf", "Total reactive energy injected L1.", "Varh"),
        "totvarhabsl1": (60, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totvarh_sf", "Total reactive energy absorbed L1.", "Varh"),
        "wl2": (64, 1, ModbusBaseClient.DATATYPE.INT16, int, "w_sf", "Active power L2.", "W"),
        "val2": (65, 1, ModbusBaseClient.DATATYPE.INT16, int, "va_sf", "Apparent power L2.", "VA"),
        "varl2": (66, 1, ModbusBaseClient.DATATYPE.INT16, int, "var_sf", "Reactive power L2.", "Var"),
        "pfl2": (67, 1, ModbusBaseClient.DATATYPE.INT16, int, "pf_sf", "Power factor L2.", ""),
        "al2": (68, 1, ModbusBaseClient.DATATYPE.INT16, int, "a_sf", "Current L2.", "A"),
        "vl2l3": (69, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase voltage L2-L3.", "V"),
        "vl2": (70, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase voltage L2-N.", "V"),
        "totwhinjl2": (71, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totwh_sf", "Total active energy injected L2.", "Wh"),
        "totwhabsl2": (75, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totwh_sf", "Total active energy absorbed L2.", "Wh"),
        "totvarhinjl2": (79, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totvarh_sf", "Total reactive energy injected L2.", "Varh"),
        "totvarhabsl2": (83, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totvarh_sf", "Total reactive energy absorbed L2.", "Varh"),
        "wl3": (87, 1, ModbusBaseClient.DATATYPE.INT16, int, "w_sf", "Active power L3.", "W"),
        "val3": (88, 1, ModbusBaseClient.DATATYPE.INT16, int, "va_sf", "Apparent power L3.", "VA"),
        "varl3": (89, 1, ModbusBaseClient.DATATYPE.INT16, int, "var_sf", "Reactive power L3.", "Var"),
        "pfl3": (90, 1, ModbusBaseClient.DATATYPE.INT16, int, "pf_sf", "Power factor L3.", ""),
        "al3": (91, 1, ModbusBaseClient.DATATYPE.INT16, int, "a_sf", "Current L3.", "A"),
        "vl3l1": (92, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase voltage L3-L1.", "V"),
        "vl3": (93, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Phase voltage L3-N.", "V"),
        "totwhinjl3": (94, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totwh_sf", "Total active energy injected L3.", "Wh"),
        "totwhabsl3": (98, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totwh_sf", "Total active energy absorbed L3.", "Wh"),
        "totvarhinjl3": (102, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totvarh_sf", "Total reactive energy injected L3.", "Varh"),
        "totvarhabsl3": (106, 4, ModbusBaseClient.DATATYPE.UINT64, int, "totvarh_sf", "Total reactive energy absorbed L3.", "Varh"),
        "throtpct": (110, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Throttling in pct of maximum active power.", "Pct"),
        "throtsrc": (111, 2, ModbusBaseClient.DATATYPE.UINT32, ThrottleSourceInformation, "", "Active throttling source.", ""),
        "a_sf": (113, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Current scale factor.", ""),
        "v_sf": (114, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Voltage scale factor.", ""),
        "hz_sf": (115, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Frequency scale factor.", ""),
        "w_sf": (116, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Active power scale factor.", ""),
        "pf_sf": (117, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Power factor scale factor.", ""),
        "va_sf": (118, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Apparent power scale factor.", ""),
        "var_sf": (119, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Reactive power scale factor.", ""),
        "totwh_sf": (120, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Active energy scale factor.", ""),
        "totvarh_sf": (121, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Reactive energy scale factor.", ""),
        "tmp_sf": (122, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Temperature scale factor.", ""),
        "mnalrminfo": (123, 32, ModbusBaseClient.DATATYPE.STRING, str, "", "Manufacturer alarm information. Valid if MANUFACTURER_ALRM indication is active.", ""),
    }
