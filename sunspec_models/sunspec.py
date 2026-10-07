from enum import IntEnum

from pymodbus.client import ModbusBaseClient


class SunSpecNotImplemented(IntEnum):
    """SunSpec NOT IMPLEMENTED values for the various types"""

    INT16 = 0x8000
    UINT16 = 0xFFFF
    INT32 = 0x80000000
    UINT32 = 0xFFFFFFFF
    INT64 = 0x8000000000000000
    UINT64 = 0xFFFFFFFFFFFFFFFF
    FLOAT32 = 0x7FC00000


class SunSpecModel:
    """The base SunSpecModel that implements all functionality"""

    _max_key_length = 2
    _max_description_length = 0

    model_description: dict[str, str] = {}

    model_map: dict[str, tuple[int, int, ModbusBaseClient.DATATYPE, type[int], str, str, str]] = {
        "id": (0, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "", ""),
        "l": (1, 1, ModbusBaseClient.DATATYPE.UINT16, int, "", "", ""),
    }

    @classmethod
    def get_value(cls, registers: list[int], map_entry: tuple[int, int, ModbusBaseClient.DATATYPE, type, str, str, str]) -> int | float | str | list[bool] | list[int] | list[float] | None:
        """Extracts a value from a list of Modbus registers"""
        offset, count, data_type, target_type, scale_factor, description, units = map_entry

        target_value = None
        not_implemented: bool = False

        converted_value = ModbusBaseClient.convert_from_registers(registers=registers[offset : offset + count], data_type=data_type)

        if isinstance(converted_value, int):
            if data_type == ModbusBaseClient.DATATYPE.INT16 and abs(converted_value) == SunSpecNotImplemented.INT16:
                not_implemented = True
            if data_type == ModbusBaseClient.DATATYPE.UINT16 and abs(converted_value) == SunSpecNotImplemented.UINT16:
                not_implemented = True
            if data_type == ModbusBaseClient.DATATYPE.INT32 and abs(converted_value) == SunSpecNotImplemented.INT32:
                not_implemented = True
            if data_type == ModbusBaseClient.DATATYPE.UINT32 and abs(converted_value) == SunSpecNotImplemented.UINT32:
                not_implemented = True
            if data_type == ModbusBaseClient.DATATYPE.INT64 and abs(converted_value) == SunSpecNotImplemented.INT64:
                not_implemented = True
            if data_type == ModbusBaseClient.DATATYPE.UINT64 and abs(converted_value) == SunSpecNotImplemented.UINT64:
                not_implemented = True
        elif isinstance(converted_value, float):
            if data_type == ModbusBaseClient.DATATYPE.FLOAT32 and abs(converted_value) == SunSpecNotImplemented.FLOAT32:
                not_implemented = True

        if not not_implemented:
            target_value = converted_value
            if target_type:
                target_value = target_type(converted_value)
                if isinstance(target_value, IntEnum):
                    target_value = target_value.name

        return target_value

    @classmethod
    def find_model_id(cls, registers: list[int]) -> int:
        """Extract the SunSpec Model id from the supplied registers"""
        key = "id"
        id: int = cls.get_value(registers=registers, map_entry=cls.model_map[key]) # type: ignore
        return id

    @classmethod
    def display(cls, registers: list[int]) -> None:
        """Print all the values of the provided registers"""
        print(" DEVICE DETAILS ".center(150, "="))

        for key in cls.model_description:
            field_name = f"[{key}]".ljust(cls._max_key_length + cls._max_description_length + 5, " ")
            v = cls.model_description[key]
            print(f"{field_name} [{v}]")

        print(" MEASUREMENTS ".center(150, "-"))
        cls.decode(registers)
        print()

    @classmethod
    def decode(cls, registers: list[int]) -> None:
        """Extract all SunSpec Model values from the supplied registers and print them"""
        for key in cls.model_map:
            map_entry = cls.model_map[key]
            offset, count, data_type, target_type, scale_factor_key, description, units = map_entry # type: ignore

            key_part = f"[{key}]".ljust(cls._max_key_length + 2, " ")
            description_part = f"[{description}]".ljust(cls._max_description_length + 2, " ")
            field_name = f"{key_part} {description_part}"

            v = cls.get_value(registers=registers, map_entry=cls.model_map[key]) # type: ignore
            if v is not None:
                # do we have a scale factor?
                if len(scale_factor_key) > 0 and v != 0:
                    scale_factor_entry = cls.model_map[scale_factor_key]
                    scale_factor = cls.get_value(registers=registers, map_entry=scale_factor_entry) # type: ignore
                    if scale_factor is not None and isinstance(scale_factor, int):
                        print(f"{field_name} [{v * (10**scale_factor):.2f}] = [{v} * (10**{scale_factor})] using scale factor [{scale_factor_key}]")
                    else:
                        print(f"{field_name} [NOT_IMPLEMENTED] scale factor not implemented")
                else:
                    print(f"{field_name} [{v}]")
            else:
                print(f"{field_name} [NOT_IMPLEMENTED]")
