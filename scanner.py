#!/usr/bin/env python3
"""
Scan SolarEdge inverters for a SunSpec Map and attached batteries.
Then print information about what was (and was not) found.

usage: scanner.py [-h] [--device-id [1-255]] host port

positional arguments:
  host                 modbus TCP address
  port                 modbus TCP port

options:
  -h, --help           show this help message and exit
  --device-id [1-255]  modbus device address (default: 1)
"""

import argparse

from pymodbus import ModbusException
from pymodbus.client import ModbusTcpClient
from pymodbus.pdu import ModbusPDU

import sunspec_models


def modbus_read(client: ModbusTcpClient, device_id: int, address: int, count: int) -> list[int]:
    """Read one or more holding registers from a Modbus server"""
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
            if not client.connected:
                print("Reconnecting to server")
                client.connect()

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


def get_value(
    registers: list[int], offset: int, count: int, data_type: ModbusTcpClient.DATATYPE
) -> int | float | str | list[bool] | list[int] | list[float]:
    """Extract the value from a list of Modbus registers"""
    return ModbusTcpClient.convert_from_registers(registers=registers[offset : offset + count], data_type=data_type)


def sunspec_found(client: ModbusTcpClient, device_id: int, address: int) -> bool:
    """Report if the SunSpec identifier was found at a specific address"""
    print(f"  Looking for SunSpec identifier at address [{address} ({hex(address)})] for device [{device_id}]")

    registers: list[int] = modbus_read(client=client, device_id=device_id, address=address, count=2)
    identifier: str = get_value(registers=registers, offset=0, count=2, data_type=ModbusTcpClient.DATATYPE.STRING)  # type: ignore

    return identifier == "SunS"


def process_sunspec_block(client: ModbusTcpClient, device_id: int, block_address: int) -> int:
    """
    Read a set of holding registers from a Modbus server.
    Then identify the SunSpec Model found and print the contents of that block.
    """
    print()
    print(f"   Reading Block at address [{block_address} ({hex(block_address)})] for device [{device_id}]")

    next_address: int = -1
    block_length: int = -1

    registers: list[int] = modbus_read(client=client, device_id=device_id, address=block_address, count=2)
    if registers:
        next_address: int = block_address + 2

        block_id: int = get_value(registers=registers, offset=0, count=1, data_type=ModbusTcpClient.DATATYPE.UINT16)  # type: ignore
        block_length: int = get_value(registers=registers, offset=1, count=1, data_type=ModbusTcpClient.DATATYPE.UINT16)  # type: ignore

        print(f"    Block id     = [{block_id}]")
        print(f"    Block length = [{block_length}]")

        if block_id == sunspec_models.SunSpecNotImplemented.UINT16:
            print("    Block type   = [The End of the block list has been reached]")
            next_address = -1
        else:
            registers = modbus_read(client=client, device_id=device_id, address=block_address, count=block_length + 2)
            if registers:
                model = sunspec_models.get_model(registers=registers)
                if model:
                    model.display(registers=registers)  # type: ignore
                else:
                    print(f"    Model not found = {registers}")
            else:
                print("    Registers     = [None]")
    else:
        print("    Registers     = [None]")

    if next_address >= 0 and block_length > 0:
        return next_address + block_length
    else:
        return -1


def process_battery(client: ModbusTcpClient, device_id: int, address: int) -> None:
    """
    Read a set of holding registers from a Modbus server.
    Then try to identify battery information and print the details.
    """
    print(f"  Looking for Battery at address [{address} ({hex(address)})] for device [{device_id}]")

    registers: list[int] = modbus_read(client=client, device_id=device_id, address=address, count=66)
    if registers:
        battery_device_id: int = get_value(registers=registers, offset=64, count=1, data_type=ModbusTcpClient.DATATYPE.UINT16)  # type: ignore

        if battery_device_id == 255 or registers[0] == 0:
            print("   No battery found at this address")
            print()
        else:
            manufacturer: str = get_value(registers=registers, offset=0, count=16, data_type=ModbusTcpClient.DATATYPE.STRING)  # type: ignore
            model: str = get_value(registers=registers, offset=16, count=16, data_type=ModbusTcpClient.DATATYPE.STRING)  # type: ignore
            firmware_version: str = get_value(registers=registers, offset=32, count=16, data_type=ModbusTcpClient.DATATYPE.STRING)  # type: ignore

            print()
            print(f"     Manufacturer     [{manufacturer}]")
            print(f"     Model            [{model}]")
            print(f"     Firmware Version [{firmware_version}]")
            print(f"     Device id        [{battery_device_id}]")

            registers = modbus_read(client=client, device_id=device_id, address=address, count=154)
            if registers:
                print(f"     Registers        {registers}")
            else:
                print("     Registers        [None]")
            print()
    else:
        print("     Registers        [None]")
        print()


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("host", type=str, help="modbus TCP address")
    argparser.add_argument("port", type=int, help="modbus TCP port")
    argparser.add_argument("--device-id", type=int, choices=range(1, 256), default=1, metavar="[1-255]", help="modbus device address (default: 1)")

    args: argparse.Namespace = argparser.parse_args()

    client = ModbusTcpClient(host=args.host, port=args.port)

    print("Connecting to server")
    client.connect()
    if client.connected:
        print()

        print(" Connected to server")
        print()

        if sunspec_found(client=client, device_id=args.device_id, address=40000):
            print("  The inverter is providing a SunSpec Map")

            address: int = 40002
            while address > 0 and client.connected:
                address = process_sunspec_block(client=client, device_id=args.device_id, block_address=address)

            print()
            print("  End of SunSpec MAP")
        else:
            print("  The inverter is NOT providing a SunSpec Map")

        print()

        process_battery(client=client, device_id=args.device_id, address=57600)
        process_battery(client=client, device_id=args.device_id, address=57856)

    if client.connected:
        client.close()
        print("Disconnected from server")
    else:
        print("Already disconnected from server")
