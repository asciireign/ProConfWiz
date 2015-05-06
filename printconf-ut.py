import untangle
config = untangle.parse('settings.xml')

Name = config.data.standort.Name.cdata
SOIP = config.data.standort.IP.cdata

VLANzahl = config.data.VLANs.Anzahl.cdata
try: 
	VLANzahl = int(VLANzahl)
except ValueError:
	VLANzahl = 1
startIP = 101
portA = 10
portB = 12

print('Standort: ' + Name)
print('IP Basis: ' + SOIP)

def vlandef(startIP,SOIP,portA,portB):
	print 'vlan', startIP
	print 'name "VLAN {}"'.format(startIP)
	print 'untagged {}-{}'.format(portA,portB)
	print 'ip adress 10.{}.{}.1 255.255.255.0'.format(SOIP,startIP)
	print 'ip helper-address 10.140.{}.10'.format(SOIP)
	print 'exit'

for x in range(0,int(VLANzahl)):
	print 'VLAN {} mit IP-Netz: 10.{}.{}.0 erstellt.'.format(startIP,SOIP,startIP)
	vlandef(startIP,SOIP,portA,portB)
	portA = portA+3
	portB = portB+3
	startIP = startIP+1
