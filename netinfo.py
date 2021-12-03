#!/usr/bin/env python3
import socket
import subprocess
import platform
import re
from requests import get

whiteSpace = ' '

def isValidIPv4Address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def getDNSIPs():
	dns_ips = []

	if(platform.system() == "Windows"):
		output = str(subprocess.check_output(["ipconfig", "-all"], encoding='utf8'))
		ipconfig_all_list = output.split('\n')

		for i in range(0, len(ipconfig_all_list)):
			if "DNS Servers" in ipconfig_all_list[i]:
				# get the first dns server ip
				first_ip = ipconfig_all_list[i].split(":")[1].strip()
				if not isValidIPv4Address(first_ip):
					continue
				dns_ips.append(first_ip)
				# get all other dns server ips if they exist
				k = i+1
				while k < len(ipconfig_all_list) and ":" not in ipconfig_all_list[k]:
					ip = ipconfig_all_list[k].strip()
					if isValidIPv4Address(ip):
						dns_ips.append(ip)
					k += 1
				# at this point we're done
				break

	else:
		with open('/etc/resolv.conf') as fp:
			for cnt, line in enumerate(fp):
				columns = line.split()
				if len(columns)>1 and columns[0] == 'nameserver':
					ip = columns[1:][0]
					if isValidIPv4Address(ip):
						dns_ips.append(ip)

	return dns_ips

def getDefaultGateway():
	if(platform.system() == "Darwin"):
		gateway = str(subprocess.check_output(["route","get","default"]))
		start = "gateway: "
		end = "\\n"
		if("gateway" in gateway):
			return gateway.split(start)[1].split(end)[0]
	else:
		import netifaces
		gateways = netifaces.gateways()
		default_gateway = gateways['default'][netifaces.AF_INET][0]
		return default_gateway
		
hostname = socket.gethostname()

default_gateway = getDefaultGateway()
DNSIPs = getDNSIPs()
formattedDNS = ""
for x in DNSIPs:
	formattedDNS += x+"\n%s" % (whiteSpace*17)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((default_gateway, 80))
local_ip = s.getsockname()[0]
s.close()
	
global_ip = get('https://api.ipify.org').text

print("Hostname:%s%s" % (whiteSpace*8, hostname))
print("Local IP:%s%s" % (whiteSpace*8, local_ip))
print("Default Gateway: "+default_gateway)
print("DNS Servers:%s%s" % (whiteSpace*5, formattedDNS.strip()))
print("Global IP:%s%s" % (whiteSpace*7, global_ip))

