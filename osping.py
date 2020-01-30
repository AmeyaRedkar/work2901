import os

ipaddresses=open("C:\\Users\\appam\\Desktop\\work2901\\workscript\\ipaddress.txt","r+")
output=open("C:\\Users\\appam\\Desktop\\work2901\\workscript\\sadaoutput.txt","w+")

ipaddresses.seek(0)

iplist1=ipaddresses.readlines()

iplist2=[x.strip('\n') for x in iplist1]

for x in iplist2:

	print "checking ip {}".format(x)

	response =os.popen("ping {}".format(x)).read()
	
	output.write("*"*60)

	output.write(response)
	

raw_input("checking done, press any key to exit")

ipaddresses.close()
output.close()

	#print "*"*60
	#os.system('ping {}'.format(x))
	#print"*"*60
	