from enum import IntFlag

from pymodbus.client import ModbusBaseClient

from .sunspec import SunSpecModel


class Model204(SunSpecModel):
    """Model definition for SunSpec Model 204 delta-connect three phase (abc) meter"""

    class Events(IntFlag):
        """Flags used in this Model"""
    
        M_EVENT_Power_Failure = 2
        M_EVENT_Under_Voltage = 3
        M_EVENT_Low_PF = 4
        M_EVENT_Over_Current = 5
        M_EVENT_Over_Voltage = 6
        M_EVENT_Missing_Sensor = 7
        M_EVENT_Reserved1 = 8
        M_EVENT_Reserved2 = 9
        M_EVENT_Reserved3 = 10
        M_EVENT_Reserved4 = 11
        M_EVENT_Reserved5 = 12
        M_EVENT_Reserved6 = 13
        M_EVENT_Reserved7 = 14
        M_EVENT_Reserved8 = 15
        M_EVENT_OEM01 = 16
        M_EVENT_OEM02 = 17
        M_EVENT_OEM03 = 18
        M_EVENT_OEM04 = 19
        M_EVENT_OEM05 = 20
        M_EVENT_OEM06 = 21
        M_EVENT_OEM07 = 22
        M_EVENT_OEM08 = 23
        M_EVENT_OEM09 = 24
        M_EVENT_OEM10 = 25
        M_EVENT_OEM11 = 26
        M_EVENT_OEM12 = 27
        M_EVENT_OEM13 = 28
        M_EVENT_OEM14 = 29
        M_EVENT_OEM15 = 30
    
    _max_key_length = 15
    _max_description_length = 53

    model_description = {
        "id": "204",
        "name": "ac_meter_abc",
        "label": "delta-connect three phase (abc) meter",
        "description": "",
    }
    
    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Model identifier", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "Model length", ""),
        "a": (2, 1, ModbusBaseClient.DATATYPE.INT16, int, "a_sf", "Total AC Current", "A"),
        "apha": (3, 1, ModbusBaseClient.DATATYPE.INT16, int, "a_sf", "Phase A Current", "A"),
        "aphb": (4, 1, ModbusBaseClient.DATATYPE.INT16, int, "a_sf", "Phase B Current", "A"),
        "aphc": (5, 1, ModbusBaseClient.DATATYPE.INT16, int, "a_sf", "Phase C Current", "A"),
        "a_sf": (6, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Current scale factor", ""),
        "phv": (7, 1, ModbusBaseClient.DATATYPE.INT16, int, "v_sf", "Line to Neutral AC Voltage (average of active phases)", "V"),
        "phvpha": (8, 1, ModbusBaseClient.DATATYPE.INT16, int, "v_sf", "Phase Voltage AN", "V"),
        "phvphb": (9, 1, ModbusBaseClient.DATATYPE.INT16, int, "v_sf", "Phase Voltage BN", "V"),
        "phvphc": (10, 1, ModbusBaseClient.DATATYPE.INT16, int, "v_sf", "Phase Voltage CN", "V"),
        "ppv": (11, 1, ModbusBaseClient.DATATYPE.INT16, int, "v_sf", "Line to Line AC Voltage (average of active phases)", "V"),
        "phvphab": (12, 1, ModbusBaseClient.DATATYPE.INT16, int, "v_sf", "Phase Voltage AB", "V"),
        "phvphbc": (13, 1, ModbusBaseClient.DATATYPE.INT16, int, "v_sf", "Phase Voltage BC", "V"),
        "phvphca": (14, 1, ModbusBaseClient.DATATYPE.INT16, int, "v_sf", "Phase Voltage CA", "V"),
        "v_sf": (15, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Voltage scale factor", ""),
        "hz": (16, 1, ModbusBaseClient.DATATYPE.INT16, int, "hz_sf", "Frequency", "Hz"),
        "hz_sf": (17, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Frequency scale factor", ""),
        "w": (18, 1, ModbusBaseClient.DATATYPE.INT16, int, "w_sf", "Total Real Power", "W"),
        "wpha": (19, 1, ModbusBaseClient.DATATYPE.INT16, int, "w_sf", "", "W"),
        "wphb": (20, 1, ModbusBaseClient.DATATYPE.INT16, int, "w_sf", "", "W"),
        "wphc": (21, 1, ModbusBaseClient.DATATYPE.INT16, int, "w_sf", "", "W"),
        "w_sf": (22, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Real Power scale factor", ""),
        "va": (23, 1, ModbusBaseClient.DATATYPE.INT16, int, "va_sf", "AC Apparent Power", "VA"),
        "vapha": (24, 1, ModbusBaseClient.DATATYPE.INT16, int, "va_sf", "", "VA"),
        "vaphb": (25, 1, ModbusBaseClient.DATATYPE.INT16, int, "va_sf", "", "VA"),
        "vaphc": (26, 1, ModbusBaseClient.DATATYPE.INT16, int, "va_sf", "", "VA"),
        "va_sf": (27, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Apparent Power scale factor", ""),
        "var": (28, 1, ModbusBaseClient.DATATYPE.INT16, int, "var_sf", "Reactive Power", "var"),
        "varpha": (29, 1, ModbusBaseClient.DATATYPE.INT16, int, "var_sf", "", "var"),
        "varphb": (30, 1, ModbusBaseClient.DATATYPE.INT16, int, "var_sf", "", "var"),
        "varphc": (31, 1, ModbusBaseClient.DATATYPE.INT16, int, "var_sf", "", "var"),
        "var_sf": (32, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Reactive Power scale factor", ""),
        "pf": (33, 1, ModbusBaseClient.DATATYPE.INT16, int, "pf_sf", "Power Factor", "Pct"),
        "pfpha": (34, 1, ModbusBaseClient.DATATYPE.INT16, int, "pf_sf", "", "Pct"),
        "pfphb": (35, 1, ModbusBaseClient.DATATYPE.INT16, int, "pf_sf", "", "Pct"),
        "pfphc": (36, 1, ModbusBaseClient.DATATYPE.INT16, int, "pf_sf", "", "Pct"),
        "pf_sf": (37, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Power Factor scale factor", ""),
        "totwhexp": (38, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totwh_sf", "Total Real Energy Exported", "Wh"),
        "totwhexppha": (40, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totwh_sf", "", "Wh"),
        "totwhexpphb": (42, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totwh_sf", "", "Wh"),
        "totwhexpphc": (44, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totwh_sf", "", "Wh"),
        "totwhimp": (46, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totwh_sf", "Total Real Energy Imported", "Wh"),
        "totwhimppha": (48, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totwh_sf", "", "Wh"),
        "totwhimpphb": (50, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totwh_sf", "", "Wh"),
        "totwhimpphc": (52, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totwh_sf", "", "Wh"),
        "totwh_sf": (54, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Real Energy scale factor", ""),
        "totvahexp": (55, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvah_sf", "Total Apparent Energy Exported", "VAh"),
        "totvahexppha": (57, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvah_sf", "", "VAh"),
        "totvahexpphb": (59, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvah_sf", "", "VAh"),
        "totvahexpphc": (61, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvah_sf", "", "VAh"),
        "totvahimp": (63, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvah_sf", "Total Apparent Energy Imported", "VAh"),
        "totvahimppha": (65, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvah_sf", "", "VAh"),
        "totvahimpphb": (67, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvah_sf", "", "VAh"),
        "totvahimpphc": (69, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvah_sf", "", "VAh"),
        "totvah_sf": (71, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Apparent Energy scale factor", ""),
        "totvarhimpq1": (72, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "Total Reactive Energy Imported Quadrant 1", "varh"),
        "totvarhimpq1pha": (74, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarhimpq1phb": (76, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarhimpq1phc": (78, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarhimpq2": (80, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "Total Reactive Power Imported Quadrant 2", "varh"),
        "totvarhimpq2pha": (82, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarhimpq2phb": (84, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarhimpq2phc": (86, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarhexpq3": (88, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "Total Reactive Power Exported Quadrant 3", "varh"),
        "totvarhexpq3pha": (90, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarhexpq3phb": (92, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarhexpq3phc": (94, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarhexpq4": (96, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "Total Reactive Power Exported Quadrant 4", "varh"),
        "totvarhexpq4pha": (98, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarhexpq4phb": (100, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarhexpq4phc": (102, 2, ModbusBaseClient.DATATYPE.UINT32, int, "totvarh_sf", "", "varh"),
        "totvarh_sf": (104, 1, ModbusBaseClient.DATATYPE.INT16, int, "", "Reactive Energy scale factor", ""),
        "evt": (105, 2, ModbusBaseClient.DATATYPE.UINT32, Events, "", "Meter Event Flags", ""),
    }
