import untangle
config = untangle.parse('settings.xml')

Name = config.data.standort.Name.cdata
IP = config.data.standort.IP.cdata

VLANzahl = config.data.VLANs.Anzahl.cdata
try: 
	VLANzahl = int(VLANzahl)
except ValueError:
	VLANzahl = 1
startIP = 101

print('Standort: ' + Name)
print('IP Basis: ' + IP)

for x in range(0,int(VLANzahl)):
	print "VLAN ", startIP,'mit IP-Netz: 10.'+IP+'.',startIP,'.0 erstellt.'
	startIP = startIP + 1
