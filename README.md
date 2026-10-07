# SolarEdge Scanner

The current version of the [Domoticz SolarEdge_ModbusTCP plugin](https://github.com/addiejanssen/domoticz-solaredge-modbustcp-plugin)
uses the [solaredge_modbus library](https://github.com/nmakel/solaredge_modbus) which has been archived by its author.

Unfortunately, the documentation of SolarEdge and the response from inverters don't always match.
We build a scanner to help us understand how SolarEdge inverters actually work.

Since SolarEdge inverters support monitoring data directly from the inverter using the SunSpec open protocol,
they do provide an option to return a map showing the devices connected to the inverter.

SolarEdge uses a vendor specific approach when it comes to batteries attached to the inverter.

This scanner tries to find the SunSpec Map and display the entries in it and then tries to find batteries and show information about them.

We are asking owners of SolarEdge inverters to run the scanner and share the output in the
[Domoticz forum](https://forum.domoticz.com/viewtopic.php?t=34039) helping us to replace the solaredge_modbus library.

## WARNING

The scanner requires a `pymodbus` version that is not compatible with the Domoticz SolarEdge ModbusTCP plugin.
Using version `3.15.0` of `pymodbus` with the plugin will break the plugin.
Using version `3.6.9` of `pymodbus` with the scanner will fail the scanner.

The scanner does not use Domoticz, nor does it understand Domoticz.
It is advised to run this in a separate Python virtual environment, in its own container or on another computer away from your Domoticz installation.

## How to use

- Download the `scanner.py` file to your computer.
- Install `pymodbus` version `3.15.0` by running `pip install pymodbus==3.15.0`.
- Run the scanner: `python scanner.py <IP address or the DNS name of the inverter> <Modbus port number>`
  - Optionally add `--device-id <number>` when the inverter setup for anything else than `1`.
- Share the output in the [Domoticz forum](https://forum.domoticz.com/viewtopic.php?t=34039)

## We have a wiki!

We will document what we have found in the wiki of this repository.
