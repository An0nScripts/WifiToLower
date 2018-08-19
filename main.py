#import usr/bin/python2
import os
from Wifi import Wifi


print "\033[32m"+"          _       ___ _____ ______      __                            "
print 		 "         | |     / (_) __(_)_  __/___  / /   ____ _      _____  _____ "
print 	 	 "         | | /| / / / /_/ / / / / __ \/ /   / __ \ | /| / / _ \/ ___/ "
print 	         "         | |/ |/ / / __/ / / / / /_/ / /___/ /_/ / |/ |/ /  __/ /     "
print 	         "         |__/|__/_/_/ /_/ /_/  \____/_____/\____/|__/|__/\___/_/      "
print 		 "                                                                      "
print 		 "                                 by An0n                              "+"\033[0;0m"
print 		 "\n "
                                                                      


bssid = raw_input("Insira o BSSID: ")
channel = raw_input("Insira o Canal: ")
interfaceRede = raw_input("Insira sua interface de rede: ")
opc = 0
wifi = Wifi(bssid, channel,interfaceRede)

while opc != 6:
	opc = input("\n 1 - Iniciar Modo Monitor \n 2 - Parar Modo Monitor \n 3 - Encontrar Redes Proximas \n 4 - Monitorar Rede Alvo \n 5 - Derrubar Rede \n 6 - Sair \n >> ")

	if opc == 1:
		wifi.iniciarModoMonitor()
	elif opc == 2:
		wifi.pararModoMonitor()

	elif opc == 3: 
		wifi.scannerRedes()

	elif opc == 4:		
		wifi.monitorarRede()

	elif opc == 5:
		wifi.derrubarRede()



