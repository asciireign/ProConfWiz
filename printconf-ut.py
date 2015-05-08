#! /usr/bin/python
import untangle
import os

config = untangle.parse('settings.xml')
Name = config.data.standort.Name.cdata
SOIP = config.data.standort.IP.cdata
VLANzahl = config.data.VLANs.Anzahl.cdata
try:
    VLANzahl = int(VLANzahl)
except ValueError:
    VLANzahl = 1
portsproVlan = config.data.VLANs.PortsProVlan.cdata
try:
    portsproVlan = int(portsproVlan)
except ValueError:
    portsproVlan = 1
startIP = 101
portA = 10
portB = portA + portsproVlan - 1

print('Standort: ' + Name)
print('IP Basis: ' + SOIP)


def vlandef(startIP, SOIP, portA, portB):
    print 'vlan', startIP
    print 'name "VLAN {}"'.format(startIP)
    print 'untagged {}-{}'.format(portA, portB)
    print 'ip address 10.{}.{}.1 255.255.255.0'.format(SOIP, startIP)
    print 'ip helper-address 10.140.{}.10'.format(SOIP)
    print 'exit'


def acldef(startIP, SOIP):
    print 'ip access-list extended "{}"'.format(startIP)
    print '   permit ip 0.0.0.0 255.255.255.255 10.{}.{}.0 0.0.0.255'.format(SOIP, startIP)
    print '   deny ip 0.0.0.0 255.255.255.255 10.{}.0.0 0.0.255.255'.format(SOIP)
    print '   permit ip 0.0.0.0 255.255.255.255 0.0.0.0 255.255.255.255'
    print '   exit'


def acl2port(startIP, portA, portB):
    for x in range(portA, (portB-portA)):
        print portA

def routeroptions():
    print 'logging 10.140.{}.10'.format(SOIP)
    print('''
logging facility local6
spanning-tree
spanning-tree protocol-version MSTP
fault-finder bad-driver sensitivity high
fault-finder bad-transceiver sensitivity high
fault-finder bad-cable sensitivity high
fault-finder too-long-cable sensitivity high
fault-finder over-bandwidth sensitivity high
fault-finder broadcast-storm sensitivity high
fault-finder loss-of-link sensitivity high
fault-finder duplex-mismatch-HDx sensitivity high
fault-finder duplex-mismatch-FDx sensitivity high
    ''')

for x in range(0, int(VLANzahl)):
    vlandef(startIP, SOIP, portA, portB)
    acldef(startIP, SOIP)
    portA = portA+portsproVlan
    portB = portB+portsproVlan
    startIP = startIP+1

routeroptions()

exit()
