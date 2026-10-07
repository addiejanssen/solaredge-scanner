from enum import IntEnum

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model704(SunSpecModel):
    """Model definition for SunSpec Model 704 DER AC Controls"""

    class PowerFactorEnableWInjEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class PowerFactorReversionEnableWInj(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class PowerFactorEnableWAbsEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class PowerFactorReversionEnableWAbs(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class LimitMaxPowerPctEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class ReversionLimitMaxPowerPctEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class SetActivePowerEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class SetActivePowerMode(IntEnum):
        """States used in this Model"""
    
        W_MAX_PCT = 0
        WATTS = 1
    
    class ReversionActivePowerEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class SetReactivePowerEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class SetReactivePowerMode(IntEnum):
        """States used in this Model"""
    
        W_MAX_PCT = 0
        VAR_MAX_PCT = 1
        VAR_AVAIL_PCT = 2
        VA_MAX_PCT = 3
        VARS = 4
    
    class ReactivePowerPriority(IntEnum):
        """States used in this Model"""
    
        ACTIVE = 0
        REACTIVE = 1
        VENDOR = 2
    
    class ReversionReactivePowerEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    class NormalRampRateReference(IntEnum):
        """States used in this Model"""
    
        A_MAX = 0
        W_MAX = 1
    
    class AntiIslandingEnable(IntEnum):
        """States used in this Model"""
    
        DISABLED = 0
        ENABLED = 1
    
    _max_key_length = 17
    _max_description_length = 91

    model_description = {
        "id": "704",
        "name": "DERCtlAC",
        "label": "DER AC Controls",
        "description": "DER AC controls model.",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER AC controls model ID.", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER AC controls model length.", ""),
        "pfwinjena": (2, 1, ModbusBaseClient.DATATYPE.UINT16, PowerFactorEnableWInjEnable, "", "Power factor enable when injecting active power.", ""),
        "pfwinjenarvrt": (3, 1, ModbusBaseClient.DATATYPE.UINT16, PowerFactorReversionEnableWInj, "", "Power factor reversion timer when injecting active power enable.", ""),
        "pfwinjrvrttms": (4, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Power factor reversion timer when injecting active power.", "Secs"),
        "pfwinjrvrtrem": (6, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Power factor reversion time remaining when injecting active power.", "Secs"),
        "pfwabsena": (8, 1, ModbusBaseClient.DATATYPE.UINT16, PowerFactorEnableWAbsEnable, "", "Power factor enable when absorbing active power.", ""),
        "pfwabsenarvrt": (9, 1, ModbusBaseClient.DATATYPE.UINT16, PowerFactorReversionEnableWAbs, "", "Power factor reversion timer when absorbing active power enable.", ""),
        "pfwabsrvrttms": (10, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Power factor reversion timer when absorbing active power.", "Secs"),
        "pfwabsrvrtrem": (12, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Power factor reversion time remaining when absorbing active power.", "Secs"),
        "wmaxlimpctena": (14, 1, ModbusBaseClient.DATATYPE.UINT16, LimitMaxPowerPctEnable, "", "Limit maximum active power percent enable.", ""),
        "wmaxlimpct": (15, 1, ModbusBaseClient.DATATYPE.UINT16, int, "wmaxlimpct_sf", "Limit maximum active power percent value.", "Pct"),
        "wmaxlimpctrvrt": (16, 1, ModbusBaseClient.DATATYPE.UINT16, int, "wmaxlimpct_sf", "Reversion limit maximum active power percent value.", "Pct"),
        "wmaxlimpctenarvrt": (17, 1, ModbusBaseClient.DATATYPE.UINT16, ReversionLimitMaxPowerPctEnable, "", "Reversion limit maximum active power percent value enable.", ""),
        "wmaxlimpctrvrttms": (18, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Limit maximum active power percent reversion time.", "Secs"),
        "wmaxlimpctrvrtrem": (20, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Limit maximum active power percent reversion time remaining.", "Secs"),
        "wsetena": (22, 1, ModbusBaseClient.DATATYPE.UINT16, SetActivePowerEnable, "", "Set active power enable.", ""),
        "wsetmod": (23, 1, ModbusBaseClient.DATATYPE.UINT16, SetActivePowerMode, "", "Set active power mode.", ""),
        "wset": (24, 2, ModbusBaseClient.DATATYPE.INT32, int, "wset_sf", "Active power setting value in watts.", "W"),
        "wsetrvrt": (26, 2, ModbusBaseClient.DATATYPE.INT32, int, "wset_sf", "Reversion active power setting value in watts.", "W"),
        "wsetpct": (28, 1, ModbusBaseClient.DATATYPE.INT16, int, "wsetpct_sf", "Active power setting value as percent.", "Pct"),
        "wsetpctrvrt": (29, 1, ModbusBaseClient.DATATYPE.INT16, int, "wsetpct_sf", "Reversion active power setting value as percent.", "Pct"),
        "wsetenarvrt": (30, 1, ModbusBaseClient.DATATYPE.UINT16, ReversionActivePowerEnable, "", "Reversion active power function enable.", ""),
        "wsetrvrttms": (31, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Set active power reversion time.", "Secs"),
        "wsetrvrtrem": (33, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Set active power reversion time remaining.", "Secs"),
        "varsetena": (35, 1, ModbusBaseClient.DATATYPE.UINT16, SetReactivePowerEnable, "", "Set reactive power enable.", ""),
        "varsetmod": (36, 1, ModbusBaseClient.DATATYPE.UINT16, SetReactivePowerMode, "", "Set reactive power mode.", ""),
        "varsetpri": (37, 1, ModbusBaseClient.DATATYPE.UINT16, ReactivePowerPriority, "", "Reactive power priority.", ""),
        "varset": (38, 2, ModbusBaseClient.DATATYPE.INT32, int, "varset_sf", "Reactive power setting value in vars.", "Var"),
        "varsetrvrt": (40, 2, ModbusBaseClient.DATATYPE.INT32, int, "varset_sf", "Reversion reactive power setting value in vars.", "Var"),
        "varsetpct": (42, 1, ModbusBaseClient.DATATYPE.INT16, int, "varsetpct_sf", "Reactive power setting value as percent.", "Pct"),
        "varsetpctrvrt": (43, 1, ModbusBaseClient.DATATYPE.INT16, int, "varsetpct_sf", "Reversion reactive power setting value as percent.", "Pct"),
        "varsetenarvrt": (44, 1, ModbusBaseClient.DATATYPE.UINT16, ReversionReactivePowerEnable, "", "Reversion reactive power function enable.", ""),
        "varsetrvrttms": (45, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Set reactive power reversion time.", "Secs"),
        "varsetrvrtrem": (47, 2, ModbusBaseClient.DATATYPE.UINT32, int, "", "Set reactive power reversion time remaining.", "Secs"),
        "wrmp": (49, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Ramp rate for increases in active power during normal generation.", "%Max/Sec"),
        "wrmpref": (50, 1, ModbusBaseClient.DATATYPE.UINT16, NormalRampRateReference, "", "Ramp rate reference unit for increases in active power or current during normal generation.", ""),
        "varrmp": (51, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Ramp rate based on max reactive power per second.", "%Max/Sec"),
        "antiislena": (52, 1, ModbusBaseClient.DATATYPE.UINT16, AntiIslandingEnable, "", "Anti-islanding enable.", ""),
        "pf_sf": (53, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Power factor scale factor.", ""),
        "wmaxlimpct_sf": (54, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Limit maximum power scale factor.", ""),
        "wset_sf": (55, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Active power scale factor.", ""),
        "wsetpct_sf": (56, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Active power pct scale factor.", ""),
        "varset_sf": (57, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Reactive power scale factor.", ""),
        "varsetpct_sf": (58, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Reactive power pct scale factor.", ""),
    }
