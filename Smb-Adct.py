#!/usr/bin/python
#coding: utf-8

import os
import commands

print(''' 
 ███████╗███╗   ███╗██████╗ 
 ██╔════╝████╗ ████║██╔══██╗
 ███████╗██╔████╔██║██████╔╝
 ╚════██║██║╚██╔╝██║██╔══██╗
 ███████║██║ ╚═╝ ██║██████╔╝
 ╚══════╝╚═╝     ╚═╝╚═════╝ Automatic Discovery and Connection Tool.
        Developed by Bruno Hedaco.
''')


print('''
##      ##    ###    ########  ##    ## #### ##    ##  ######   
##  ##  ##   ## ##   ##     ## ###   ##  ##  ###   ## ##    ##  
##  ##  ##  ##   ##  ##     ## ####  ##  ##  ####  ## ##        
##  ##  ## ##     ## ########  ## ## ##  ##  ## ## ## ##   #### 
##  ##  ## ######### ##   ##   ##  ####  ##  ##  #### ##    ##  
##  ##  ## ##     ## ##    ##  ##   ###  ##  ##   ### ##    ##  
 ###  ###  ##     ## ##     ## ##    ## #### ##    ##  ######
      TO USE HEDACO'S SMB ADCT YOU'LL NEED SMB OS COMMANDS.
                    LINUX IS RECOMMENDED.
        
 This tool can be used to exploit Samba Servers all over the planet,
but that was not my main objective while developing this command automation tool.
 My recomendation for those who will use this "tool", is to only use it to facilitate
Samba connections or make life easier while connecting to Samba Servers, without the need
of typing the same commands all over again.

''')

print ("Hedaco's SAMBA TOOL")
print ("\n")
print ("\nIP smb:"),
ip = raw_input()
print ("\n")
print ("\nUsar proxychains? (Y/N):"),
pchains = raw_input()

if pchains == 'Y' or pchains =='y':
	print ("\n")
	print ("Listando pastas...")
	print ("\n")
	os.system("proxychains smbclient -L " + ip + " -N")
	print ("\n ")
elif pchains == 'N' or pchains == 'n':
	print ("\n")
	print ("Listando pastas...")
	print ("\n ")
	os.system("smbclient -L " + ip + " -N")
	print ("\n ")
	
print ("\nSharename:"),
sn = raw_input()
print ("\n ")

if pchains == 'Y' or pchains =='y':
	print ("\n")	
	print ("\nPasta ") + sn
	os.system("proxychains smbclient //" + ip + "/" + sn +" -N")
	print ("\n")
elif pchains == 'N' or pchains == 'n':
	print ("\n ")
	print ("\nPasta >") + sn
	print ("\n ")
	os.system("smbclient //" + ip + "/" + sn +" -N")
	print ("\n ")







