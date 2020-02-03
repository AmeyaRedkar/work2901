from netmiko import ConnectHandler
from configparser import ConfigParser

config=ConfigParser()
config.read("C:\\Users\\appam\\Desktop\\work2901\\configuration.txt")

vendor=["netmiko"]["vendor"]
username=["netmiko"]["username"]
password=["netmiko"]["password"]
ipaddresses=open("C:\\Users\\appam\\Desktop\\work2901\\workscript\\ipaddress.txt","r+")
result=open("C:\\Users\\appam\\Desktop\\work2901\\workscript\\sadaoutput.txt","w+")

paddresses.seek(0)
iplist1=ipaddresses.readline()
iplist2=[x.strip('\n') for x in iplist1]

for ip in iplist2:

	connection=ConnectHandler(
		"device_type":vendor,
		"host":ip,
		"username":username,
		"password":password,
		#"port":optional
		#"secret":optional
		)

	output = connection.send_command("ping {}".format(ip))

	result.write("*"*60)
	result.write(output)

ipaddresses.close()
result.close()
	