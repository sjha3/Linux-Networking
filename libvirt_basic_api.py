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
