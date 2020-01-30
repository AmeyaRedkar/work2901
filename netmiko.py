from paramiko import SSHClient, AutoAddPolicy
from configparser import ConfigParser


config=ConfigParser()
config.read("C:\\Users\\appam\\Desktop\\work2901\\configuration.txt")
user=config["sshtest"]["username"]
passwd=config["sshtest"]["password"]

ipaddresses=open("C:\\Users\\appam\\Desktop\\work2901\\workscript\\ipaddress.txt","r+")

sshoutput=open("C:\\Users\\appam\\Desktop\\work2901\\workscript\\sshoutput.txt","w+")

erroutput=open("C:\\Users\\appam\\Desktop\\work2901\\workscript\\erroutput.txt","w+")

ipaddresses.seek(0)

iplist1=ipaddresses.readline()

iplist2=[x.strip('\n') for x in iplist1]

session=SSHClient()

session.set_missing_host_key_policy(AutoAddPolicy())


for ip in iplist2:
	print "checking ip {}".format(ip)

	session.connect(ip, username = user, password = passwd)

	stdin, stdout, stderr = session.exec_command("ping {}".format(ip))

	output=stdout.readlines()
	
	error=stderr.readlines()

	for op in output:
		sshoutput.write(op)

	sshoutput.write("*"*60)

	for er in error:
		erroutput.write(er)

	erroutput.write("*"*60)


session.close()

ipaddresses.close()
sshoutput.close()
erroutput.close()




	

