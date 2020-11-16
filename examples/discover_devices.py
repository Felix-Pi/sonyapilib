"""Example to discover services on a device."""
from sonyapilib.ssdp import SSDPDiscovery

ssdp = SSDPDiscovery()
services = ssdp.discover()
for service in services:
    print(service)
