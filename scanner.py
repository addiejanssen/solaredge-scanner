#!/usr/bin/env python3
"""
Scan SolarEdge inverters for a SunSpec Map and attached batteries.
Then print information about what was (and was not) found.

usage: scanner.py [-h] [--device-id [1-255]] [--dump-registers] host port

positional arguments:
  host                 modbus TCP address
  port                 modbus TCP port

options:
  -h, --help           show this help message and exit
  --device-id [1-255]  modbus device address (default: 1)
  --do-not-dump-registers
                        do not dump modbus registers in output
"""

import argparse
import pymodbus.client as ModbusClient
from pymodbus import ModbusException
from pymodbus.pdu import ModbusPDU


def modbus_read(client: ModbusClient.ModbusTcpClient, device_id: int, address: int, count: int) -> list[int]:

    result: list[int] = []
    start: int = address
    end: int = address + count
    read_now: int

    # read_holding_registers only allows 125 registers in one go
    # we need to loop if we have more to read than that

    while start < end:
        if end - start > 125:
            read_now = 125
        else:
            read_now = end - start

        try:
            rr: ModbusPDU = client.read_holding_registers(address=start, count=read_now, device_id=device_id)
        except ModbusException as exc:
            print(f"Received ModbusException({exc}) from library")
            return []
        if rr.isError():
            print(f"Received exception from device ({rr})")
            return []

        if len(rr.registers) != read_now:
            print(f"expected [{read_now}] got [{len(rr.registers)}]")

        start += read_now
        result.extend(rr.registers)

    return result


def get_value(registers: list[int], offset:int, count:int, data_type: ModbusClient.ModbusTcpClient.DATATYPE) -> int | float | str | list[bool] | list[int] | list[float]:

    return client.convert_from_registers(registers=registers[offset:offset+count], data_type=data_type)


def sunspec_found(client: ModbusClient.ModbusTcpClient, device_id: int, address: int) -> bool:

    print(f"  Looking for SunSpec identifier at address [{address} ({hex(address)})] for device [{device_id}]")

    registers: list[int] = modbus_read(client=client, device_id=device_id, address=address, count=2)
    identifier: str = get_value(registers=registers, offset=0, count=2, data_type=ModbusClient.ModbusTcpClient.DATATYPE.STRING)  # type: ignore

    return identifier == "SunS"


def display_common_block(client: ModbusClient.ModbusTcpClient, device_id: int, start_address: int) -> None:

    registers = modbus_read(client=client, device_id=device_id, address=start_address, count=66)

    manufacturer:str = get_value(registers=registers, offset=0, count=16, data_type=ModbusClient.ModbusTcpClient.DATATYPE.STRING) # type: ignore
    model:str = get_value(registers=registers, offset=16, count=16, data_type=ModbusClient.ModbusTcpClient.DATATYPE.STRING) # type: ignore
    options:str = get_value(registers=registers, offset=32, count=8, data_type=ModbusClient.ModbusTcpClient.DATATYPE.STRING) # type: ignore
    version:str = get_value(registers=registers, offset=40, count=8, data_type=ModbusClient.ModbusTcpClient.DATATYPE.STRING) # type: ignore
    device_address:int = get_value(registers=registers, offset=64, count=1, data_type=ModbusClient.ModbusTcpClient.DATATYPE.UINT16) # type: ignore

    print(f"     Manufacturer:   [{manufacturer}]")
    print(f"     Model:          [{model}]")
    print(f"     Options:        [{options}]")
    print(f"     Version:        [{version}]")
    print(f"     Device Address: [{device_address}]")


def process_sunspec_block(client: ModbusClient.ModbusTcpClient, device_id: int, block_address: int, dump: bool = False) -> int:

    print()
    print(f"   Reading Block at address [{block_address} ({hex(block_address)})] for device [{device_id}]")

    registers: list[int] = modbus_read(client=client, device_id=device_id, address=block_address, count=2)
    next_address: int = block_address + 2

    block_id: int = get_value(registers=registers, offset=0, count=1, data_type=ModbusClient.ModbusTcpClient.DATATYPE.UINT16) # type: ignore
    block_length: int = get_value(registers=registers, offset=1, count=1, data_type=ModbusClient.ModbusTcpClient.DATATYPE.UINT16) # type: ignore

    print(f"    Block id     = [{block_id}]")
    print(f"    Block length = [{block_length}]")

    match block_id:
        case 65535:
            print("    Block type   = [The End of the block list has been reached]")
            next_address = -1
        case 1:
            print("    Block type   = [Common - All SunSpec compliant devices must include this as the first model]")
            display_common_block(client=client, device_id=device_id, start_address=next_address)
        case 2:
            print("    Block type   = [Basic Aggregator - Aggregates a collection of models for a given model id]")
        case 3:
            print("    Block type   = [Secure Dataset Read Request - Request a digital signature over a specified set of data registers]")
        case 4:
            print("    Block type   = [Secure Dataset Read Response - Compute a digital signature over a specified set of data registers]")
        case 5:
            print("    Block type   = [Secure Write Request - Include a digital signature along with the control data]")
        case 6:
            print("    Block type   = [Secure Write Sequential Request - Include a digital signature along with the control data]")
        case 7:
            print("    Block type   = [Secure Write Response Model (DRAFT 1) - Include a digital signature over the response]")
        case 8:
            print("    Block type   = [Get Device Security Certificate - Security model for PKI]")
        case 9:
            print("    Block type   = [Set Operator Security Certificate - Security model for PKI]")
        case 10:
            print("    Block type   = [Communication Interface Header - To be included first for a complete interface description]")
        case 11:
            print("    Block type   = [Ethernet Link Layer - Include to support a wired ethernet port]")
        case 12:
            print("    Block type   = [IPv4 - Include to support an IPv4 protocol stack on this interface]")
        case 13:
            print("    Block type   = [IPv6 - Include to support an IPv6 protocol stack on this interface]")
        case 14:
            print("    Block type   = [Proxy Server - Include this block to allow for a proxy server]")
        case 15:
            print("    Block type   = [Interface Counters Model - Interface counters]")
        case 16:
            print("    Block type   = [Simple IP Network - Include this model for a simple IPv4 network stack]")
        case 17:
            print("    Block type   = [Serial Interface - Include this model for serial interface configuration support]")
        case 18:
            print("    Block type   = [Cellular Link - Include this model to support a cellular interface link]")
        case 19:
            print("    Block type   = [PPP Link - Include this model to configure a Point-to-Point Protocol link]")
        case 101:
            print("    Block type   = [Inverter (Single Phase) - Include this model for single phase inverter monitoring]")
        case 102:
            print("    Block type   = [Inverter (Split-Phase) - Include this model for split phase inverter monitoring]")
        case 103:
            print("    Block type   = [Inverter (Three Phase) - Include this model for three phase inverter monitoring]")
        case 111:
            print("    Block type   = [Inverter (Single Phase) FLOAT - Include this model for single phase inverter monitoring using float values]")
        case 112:
            print("    Block type   = [Inverter (Split Phase) FLOAT - Include this model for split phase inverter monitoring using float values]")
        case 113:
            print("    Block type   = [Inverter (Three Phase) FLOAT - Include this model for three phase inverter monitoring using float values]")
        case 120:
            print("    Block type   = [Nameplate - Inverter Controls Nameplate Ratings ]")
        case 121:
            print("    Block type   = [Basic Settings - Inverter Controls Basic Settings ]")
        case 122:
            print("    Block type   = [Measurements_Status - Inverter Controls Extended Measurements and Status ]")
        case 123:
            print("    Block type   = [Immediate Controls - Immediate Inverter Controls ]")
        case 124:
            print("    Block type   = [Storage - Basic Storage Controls ]")
        case 125:
            print("    Block type   = [Pricing - Pricing Signal  ]")
        case 126:
            print("    Block type   = [Static Volt-VAR - Static Volt-VAR Arrays ]")
        case 127:
            print("    Block type   = [Freq-Watt Param - Parameterized Frequency-Watt ]")
        case 128:
            print("    Block type   = [Dynamic Reactive Current - Dynamic Reactive Current ]")
        case 129:
            print("    Block type   = [LVRTD - LVRT Must Disconnect]")
        case 130:
            print("    Block type   = [HVRTD - HVRT Must Disconnect]")
        case 131:
            print("    Block type   = [Watt-PF - Watt-Power Factor ]")
        case 132:
            print("    Block type   = [Volt-Watt - Volt-Watt ]")
        case 133:
            print("    Block type   = [Basic Scheduling - Basic Scheduling ]")
        case 134:
            print("    Block type   = [Freq-Watt Crv - Curve-Based Frequency-Watt ]")
        case 135:
            print("    Block type   = [LFRT - Low Frequency Ride-through]")
        case 136:
            print("    Block type   = [HFRT - High Frequency Ride-through]")
        case 137:
            print("    Block type   = [LVRTC - LVRT must remain connected]")
        case 138:
            print("    Block type   = [HVRTC - HVRT must remain connected]")
        case 139:
            print("    Block type   = [LVRTX - LVRT extended curve]")
        case 140:
            print("    Block type   = [HVRTX - HVRT extended curve]")
        case 141:
            print("    Block type   = [LFRTC - LFRT must remain connected]")
        case 142:
            print("    Block type   = [HFRTC - HFRT must remain connected]")
        case 143:
            print("    Block type   = [LFRTX - LFRT extended curve]")
        case 144:
            print("    Block type   = [HFRTX - HFRT extended curve]")
        case 145:
            print("    Block type   = [Extended Settings - Inverter controls extended settings ]")
        case 160:
            print("    Block type   = [Multiple MPPT Inverter Extension Model]")
        case 201:
            print("    Block type   = [Meter (Single Phase) single phase (AN or AB) meter - Include this model for single phase (AN or AB) metering]")
        case 202:
            print("    Block type   = [split single phase (ABN) meter]")
        case 203:
            print("    Block type   = [wye-connect three phase (abcn) meter]")
        case 204:
            print("    Block type   = [delta-connect three phase (abc) meter]")
        case 211:
            print("    Block type   = [single phase (AN or AB) meter]")
        case 212:
            print("    Block type   = [split single phase (ABN) meter]")
        case 213:
            print("    Block type   = [wye-connect three phase (abcn) meter]")
        case 214:
            print("    Block type   = [delta-connect three phase (abc) meter]")
        case 220:
            print("    Block type   = [Secure AC Meter Selected Readings - Include this model for secure metering]")
        case 302:
            print("    Block type   = [Irradiance Model - Include to support various irradiance measurements]")
        case 303:
            print("    Block type   = [Back of Module Temperature Model - Include to support variable number of  back of module temperature measurements]")
        case 304:
            print("    Block type   = [Inclinometer Model - Include to support orientation measurements]")
        case 305:
            print("    Block type   = [GPS - Include to support location measurements]")
        case 306:
            print("    Block type   = [Reference Point Model - Include to support a standard reference point]")
        case 307:
            print("    Block type   = [Base Met - Base Meteorological Model]")
        case 308:
            print("    Block type   = [Mini Met Model - Include to support a few basic measurements]")
        case 401:
            print("    Block type   = [String Combiner (Current) - A basic string combiner]")
        case 402:
            print("    Block type   = [String Combiner (Advanced) - An advanced string combiner]")
        case 403:
            print("    Block type   = [String Combiner (Current) - A basic string combiner model]")
        case 404:
            print("    Block type   = [String Combiner (Advanced) - An advanced string combiner including voltage and energy measurements]")
        case 501:
            print("    Block type   = [Solar Module - A solar module model supporting DC-DC converter]")
        case 502:
            print("    Block type   = [Solar Module - A solar module model supporting DC-DC converter]")
        case 601:
            print("    Block type   = [Tracker Controller DRAFT 2 - Monitors and controls multiple trackers]")
        case 701:
            print("    Block type   = [DER AC Measurement - DER AC measurement model.]")
        case 702:
            print("    Block type   = [DER Capacity - DER capacity model.]")
        case 703:
            print("    Block type   = [Enter Service - Enter service model.]")
        case 704:
            print("    Block type   = [DER AC Controls - DER AC controls model.]")
        case 705:
            print("    Block type   = [DER Volt-Var - DER Volt-Var model.]")
        case 706:
            print("    Block type   = [DER Volt-Watt - DER Volt-Watt model.]")
        case 707:
            print("    Block type   = [DER Trip LV - DER low voltage trip model.]")
        case 708:
            print("    Block type   = [DER Trip HV - DER high voltage trip model.]")
        case 709:
            print("    Block type   = [DER Trip LF - DER low frequency trip model.]")
        case 710:
            print("    Block type   = [DER Trip HF - DER high frequency trip model.]")
        case 711:
            print("    Block type   = [DER Frequency Droop - DER Frequency Droop model.]")
        case 712:
            print("    Block type   = [DER Watt-Var - DER Watt-Var model.]")
        case 713:
            print("    Block type   = [DER Storage Capacity - DER storage capacity.]")
        case 714:
            print("    Block type   = [DER DC Measurement - DER DC measurement.]")
        case 715:
            print("    Block type   = [DERCtl - DER Control]")
        case 801:
            print("    Block type   = [Energy Storage Base Model (DEPRECATED) - This model has been deprecated.]")
        case 802:
            print("    Block type   = [Battery Base Model]")
        case 803:
            print("    Block type   = [Lithium-Ion Battery Bank Model]")
        case 804:
            print("    Block type   = [Lithium-Ion String Model]")
        case 805:
            print("    Block type   = [Lithium-Ion Module Model]")
        case 806:
            print("    Block type   = [Flow Battery Model]")
        case 807:
            print("    Block type   = [Flow Battery String Model]")
        case 808:
            print("    Block type   = [Flow Battery Module Model]")
        case 809:
            print("    Block type   = [Flow Battery Stack Model]")
        case _:
            print("    Block type   = [Unknown]")

    if next_address >= 0 and block_length > 0:
        if dump:
            registers = modbus_read(client=client, device_id=device_id, address=block_address, count=block_length+2)
            if registers:
                print(f"    Registers    = {registers}")
            else:
                print("    Registers    = [None]")

        return next_address + block_length
    else:
        return -1


def process_battery(client: ModbusClient.ModbusTcpClient, device_id: int, address: int, dump: bool = False) -> None:

    print(f"  Looking for Battery at address [{address} ({hex(address)})] for device [{device_id}]")

    registers: list[int] = modbus_read(client=client, device_id=device_id, address=address, count=66)
    battery_device_id: int = get_value(registers=registers, offset=64, count=1, data_type=ModbusClient.ModbusTcpClient.DATATYPE.UINT16)  # type: ignore

    if battery_device_id == 255 or registers[0] == 0:
        print("   No battery found at this address")
        print()
    else:
        manufacturer:str = get_value(registers=registers, offset=0, count=16, data_type=ModbusClient.ModbusTcpClient.DATATYPE.STRING)  # type: ignore
        model:str = get_value(registers=registers, offset=16, count=16, data_type=ModbusClient.ModbusTcpClient.DATATYPE.STRING)  # type: ignore
        firmware_version:str = get_value(registers=registers, offset=32, count=16, data_type=ModbusClient.ModbusTcpClient.DATATYPE.STRING)  # type: ignore

        print()
        print(f"     Manufacturer     [{manufacturer}]")
        print(f"     Model            [{model}]")
        print(f"     Firmware Version [{firmware_version}]")
        print(f"     Device id        [{battery_device_id}]")

        if dump:
            registers = modbus_read(client=client, device_id=device_id, address=address, count=410)
            if registers:
                print(f"     Registers        {registers}")
            else:
                print("     Registers        [None]")
        print()


if __name__ == "__main__":

    argparser = argparse.ArgumentParser()
    argparser.add_argument("host", type=str, help="modbus TCP address")
    argparser.add_argument("port", type=int, help="modbus TCP port")
    argparser.add_argument("--device-id", type=int, choices=range(1, 256), default=1, metavar="[1-255]", help="modbus device address (default: 1)")
    argparser.add_argument("--do-not-dump-registers", action='store_false', help="do not dump modbus registers in output")

    args: argparse.Namespace = argparser.parse_args()

    client = ModbusClient.ModbusTcpClient(host=args.host, port=args.port)

    print("Connecting to server")
    client.connect()
    if client.connected:
        print()

        print(" Connected to server")
        print()

        if sunspec_found(client = client, device_id=args.device_id, address=40000):
            print("  The inverter is providing a SunSpec Map")

            address: int = 40002
            while address > 0 and client.connected:
                address = process_sunspec_block(client=client, device_id=args.device_id, block_address=address, dump=args.do_not_dump_registers)

            print()
            print("  End of SunSpec MAP")
        else:
            print("  The inverter is NOT providing a SunSpec Map")

        print()

        process_battery(client=client, device_id=args.device_id, address=57600, dump=args.do_not_dump_registers)
        process_battery(client=client, device_id=args.device_id, address=57856, dump=args.do_not_dump_registers)

    if client.connected:
        client.close()
        print("Disconnected from server")
    else:
        print("Already disconnected from server")
