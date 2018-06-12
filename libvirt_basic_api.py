import sys
import libvirt
conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system')
    exit(1)
else :
    print("Yayyy")
print(str(conn))
#print(conn.getCapabilities())
print("Hostbame : ", conn.getHostname())
print("Max CPUs: ",conn.getMaxVcpus(None))
print("Type: ",conn.getType())
print("Version: ",conn.getVersion())
print("LibVersion: ",conn.getLibVersion())
print("URI: ",conn.getURI())
print("Sysinfo: ",conn.getSysinfo)
print("CPUMAP: ",conn.getCPUMap)
print("CPUStats: ",conn.getCPUStats(0))


domains = conn.listDomainsID()
if domains != None:
    print domains
    for i in domains:
       domain = conn.lookupByID(i)
       print("UUID of domain:", i , ":", domain.UUIDString())
conn.close()
exit(0)

'''  =========== OUTPUT =============
<libvirt.virConnect object at 0x7f35d96377d0>
('Hostbame : ', 'bn20-24.dcs.mcnc.org')
('Max CPUs: ', 16)
('Type: ', 'QEMU')
('Version: ', 2005000)
('LibVersion: ', 1003001)
('URI: ', 'qemu:///system')
('Sysinfo: ', <bound method virConnect.getSysinfo of <libvirt.virConnect object at 0x7f35d96377d0>>)
('CPUMAP: ', <bound method virConnect.getCPUMap of <libvirt.virConnect object at 0x7f35d96377d0>>)
('CPUStats: ', {'kernel': 1693240000000L, 'idle': 464898130000000L, 'user': 4863390000000L, 'iowait': 110380000000L})
[13, 10, 8, 15]
('UUID of domain:', 13, ':', '82f8907c-4ff0-4161-a7c2-6ef9510628a2')
('UUID of domain:', 10, ':', 'aa93d25f-515e-4dee-8c6e-1786c221ce50')
('UUID of domain:', 8, ':', '8405fa44-5da9-4632-9208-8c3d8c467c49')
('UUID of domain:', 15, ':', '2621642e-754a-45e6-8f0c-c9cec9111bdb')
'''
