import os
sizeFile=os.path.getsize("one.jpg")

for i in range(0,sizeFile):
	file2write=open("mutaded\\onewrited%d.jpg"%i,"wb")
	with open("one.jpg","rb") as f:
		ibyte=0
		while 1:
			byte_s=f.read(1)
			#print str(ord(byte_s))+" "+str(ord(byte_s)>>2)
			# print "ibyte="+str(ibyte)
			# print "i="+str(i)
			# print "byte_s="+str(byte_s)
			if not byte_s:
				break
			if ibyte==i:
				#print byte_s[:-1]+ " "+chr(ord(byte_s[-1]))
				#print "zmiana bajtu %d"%ibyte
				file2write.write(byte_s[:-1]+chr((ord(byte_s[-1])-1) % 255))
			else:
				#print "bez zmiany bajtu %d"%ibyte
				file2write.write(byte_s)
			ibyte=ibyte+1
	file2write.close()