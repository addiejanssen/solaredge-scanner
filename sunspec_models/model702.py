from enum import IntEnum, IntFlag

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model702(SunSpecModel):
    """Model definition for SunSpec Model 702 DER Capacity"""

    class NormalOperatingCategory(IntEnum):
        """States used in this Model"""
    
        CAT_A = 0
        CAT_B = 1
    
    class AbnormalOperatingCategory(IntEnum):
        """States used in this Model"""
    
        CAT_1 = 0
        CAT_2 = 1
        CAT_3 = 2
    
    class SupportedControlModes(IntFlag):
        """Flags used in this Model"""
    
        MAX_W = 0
        FIXED_W = 1
        FIXED_VAR = 2
        FIXED_PF = 3
        VOLT_VAR = 4
        FREQ_WATT = 5
        DYN_REACT_CURR = 6
        LV_TRIP = 7
        HV_TRIP = 8
        WATT_VAR = 9
        VOLT_WATT = 10
        SCHEDULED = 11
        LF_TRIP = 12
        HF_TRIP = 13
    
    class IntentionalIslandCategories(IntFlag):
        """Flags used in this Model"""
    
        UNCATEGORIZED = 0
        INT_ISL_CAPABLE = 1
        BLACK_START_CAPABLE = 2
        ISOCH_CAPABLE = 3
    
    class IntentionalIslandCategories(IntFlag):
        """Flags used in this Model"""
    
        UNCATEGORIZED = 0
        INT_ISL_CAPABLE = 1
        BLACK_START_CAPABLE = 2
        ISOCH_CAPABLE = 3
    
    _max_key_length = 17
    _max_description_length = 106

    model_description = {
        "id": "702",
        "name": "DERCapacity",
        "label": "DER Capacity",
        "description": "DER capacity model.",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER capacity model ID.", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "DER capacity model length.", ""),
        "wmaxrtg": (2, 1, ModbusBaseClient.DATATYPE.UINT16, int, "w_sf", "Maximum active power rating at unity power factor in watts.", "W"),
        "wovrextrtg": (3, 1, ModbusBaseClient.DATATYPE.UINT16, int, "w_sf", "Active power rating at specified over-excited power factor in watts.", "W"),
        "wovrextrtgpf": (4, 1, ModbusBaseClient.DATATYPE.UINT16, int, "pf_sf", "Specified over-excited power factor.", ""),
        "wundextrtg": (5, 1, ModbusBaseClient.DATATYPE.UINT16, int, "w_sf", "Active power rating at specified under-excited power factor in watts.", "W"),
        "wundextrtgpf": (6, 1, ModbusBaseClient.DATATYPE.UINT16, int, "pf_sf", "Specified under-excited power factor.", ""),
        "vamaxrtg": (7, 1, ModbusBaseClient.DATATYPE.UINT16, int, "va_sf", "Maximum apparent power rating in voltamperes.", "VA"),
        "varmaxinjrtg": (8, 1, ModbusBaseClient.DATATYPE.UINT16, int, "var_sf", "Maximum injected reactive power rating in vars.", "Var"),
        "varmaxabsrtg": (9, 1, ModbusBaseClient.DATATYPE.UINT16, int, "var_sf", "Maximum absorbed reactive power rating in vars.", "Var"),
        "wchartemaxrtg": (10, 1, ModbusBaseClient.DATATYPE.UINT16, int, "w_sf", "Maximum active power charge rate in watts.", "W"),
        "wdischartemaxrtg": (11, 1, ModbusBaseClient.DATATYPE.UINT16, int, "w_sf", "Maximum active power discharge rate in watts.", "W"),
        "vachartemaxrtg": (12, 1, ModbusBaseClient.DATATYPE.UINT16, int, "va_sf", "Maximum apparent power charge rate in voltamperes.", "VA"),
        "vadischartemaxrtg": (13, 1, ModbusBaseClient.DATATYPE.UINT16, int, "va_sf", "Maximum apparent power discharge rate in voltamperes.", "VA"),
        "vnomrtg": (14, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "AC voltage nominal rating.", "V"),
        "vmaxrtg": (15, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "AC voltage maximum rating.", "V"),
        "vminrtg": (16, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "AC voltage minimum rating.", "V"),
        "amaxrtg": (17, 1, ModbusBaseClient.DATATYPE.UINT16, int, "a_sf", "AC current maximum rating in amps.", "A"),
        "pfovrextrtg": (18, 1, ModbusBaseClient.DATATYPE.UINT16, int, "pf_sf", "Unused. Please use WOvrExtRtgPF.", ""),
        "pfundextrtg": (19, 1, ModbusBaseClient.DATATYPE.UINT16, int, "pf_sf", "Unused. Please use WUndExtRtgPF.", ""),
        "reactsusceptrtg": (20, 1, ModbusBaseClient.DATATYPE.UINT16, int, "s_sf", "Reactive susceptance that remains connected to the Area EPS in the cease to energize and trip state.", "S"),
        "noropcatrtg": (21, 1, ModbusBaseClient.DATATYPE.UINT16, NormalOperatingCategory, "", "Normal operating performance category as specified in IEEE 1547-2018.", ""),
        "abnopcatrtg": (22, 1, ModbusBaseClient.DATATYPE.UINT16, AbnormalOperatingCategory, "", "Abnormal operating performance category as specified in IEEE 1547-2018.", ""),
        "ctrlmodes": (23, 2, ModbusBaseClient.DATATYPE.UINT32, SupportedControlModes, "", "Supported control mode functions.", ""),
        "intislandcatrtg": (25, 1, ModbusBaseClient.DATATYPE.UINT16, IntentionalIslandCategories, "", "Intentional island categories.", ""),
        "wmax": (26, 1, ModbusBaseClient.DATATYPE.UINT16, int, "w_sf", "Maximum active power setting used to adjust maximum active power setting.", "W"),
        "wmaxovrext": (27, 1, ModbusBaseClient.DATATYPE.UINT16, int, "w_sf", "Active power setting at specified over-excited power factor in watts.", "W"),
        "wovrextpf": (28, 1, ModbusBaseClient.DATATYPE.UINT16, int, "pf_sf", "Specified over-excited power factor.", ""),
        "wmaxundext": (29, 1, ModbusBaseClient.DATATYPE.UINT16, int, "w_sf", "Active power setting at specified under-excited power factor in watts.", "W"),
        "wundextpf": (30, 1, ModbusBaseClient.DATATYPE.UINT16, int, "pf_sf", "Specified under-excited power factor.", ""),
        "vamax": (31, 1, ModbusBaseClient.DATATYPE.UINT16, int, "va_sf", "Maximum apparent power setting used to adjust maximum apparent power rating.", "VA"),
        "varmaxinj": (32, 1, ModbusBaseClient.DATATYPE.UINT16, int, "var_sf", "Maximum injected reactive power setting used to adjust maximum injected reactive power rating.", "Var"),
        "varmaxabs": (33, 1, ModbusBaseClient.DATATYPE.UINT16, int, "var_sf", "Maximum absorbed reactive power setting used to adjust maximum absorbed reactive power rating.", "Var"),
        "wchartemax": (34, 1, ModbusBaseClient.DATATYPE.UINT16, int, "w_sf", "Maximum active power charge rate setting used to adjust maximum active power charge rate rating.", "W"),
        "wdischartemax": (35, 1, ModbusBaseClient.DATATYPE.UINT16, int, "w_sf", "Maximum active power discharge rate setting used to adjust maximum active power discharge rate rating.", "W"),
        "vachartemax": (36, 1, ModbusBaseClient.DATATYPE.UINT16, int, "va_sf", "Maximum apparent power charge rate setting used to adjust maximum apparent power charge rate rating.", "VA"),
        "vadischartemax": (37, 1, ModbusBaseClient.DATATYPE.UINT16, int, "va_sf", "Maximum apparent power discharge rate setting used to adjust maximum apparent power discharge rate rating.", "VA"),
        "vnom": (38, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "Nominal AC voltage setting.", "V"),
        "vmax": (39, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "AC voltage maximum setting used to adjust AC voltage maximum rating.", "V"),
        "vmin": (40, 1, ModbusBaseClient.DATATYPE.UINT16, int, "v_sf", "AC voltage minimum setting used to adjust AC voltage minimum rating.", "V"),
        "amax": (41, 1, ModbusBaseClient.DATATYPE.UINT16, int, "a_sf", "Maximum AC current setting used to adjust maximum AC current rating.", "A"),
        "pfovrext": (42, 1, ModbusBaseClient.DATATYPE.UINT16, int, "pf_sf", "Unused. Please use WOvrExtPF.", ""),
        "pfundext": (43, 1, ModbusBaseClient.DATATYPE.UINT16, int, "pf_sf", "Unused. Please use WUndExtPF.", ""),
        "intislandcat": (44, 1, ModbusBaseClient.DATATYPE.UINT16, IntentionalIslandCategories, "", "Intentional island categories.", ""),
        "w_sf": (45, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Active power scale factor.", ""),
        "pf_sf": (46, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Power factor scale factor.", ""),
        "va_sf": (47, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Apparent power scale factor.", ""),
        "var_sf": (48, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Reactive power scale factor.", ""),
        "v_sf": (49, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Voltage scale factor.", ""),
        "a_sf": (50, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Current scale factor.", ""),
        "s_sf": (51, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Susceptance scale factor.", ""),
    }
