#!/bin/python3
import sys
import socket
import information
import requests
from requests_html import HTMLSession
import os

print ("\n\n\n=============****   PYTHON PORT SCANVAGANZA  ****=============")
print ("=============****           VERSION 3        ****=============")
print ("=============****                            ****=============")
print ("=============****  INSERT YOUR HOST AND WAIT ****=============")
print ("=============****                            ****=============")
print ("=============************************************=============\n")

open_ports = []

host = input("\n Please, insert the host name ---> ")
alpha = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,y,w,z"

try:
    socket.gethostbyname(host)
except socket.gaierror:
    print ("\nOoops!\n\n",host," Inexists. <---\n\n")
    sys.exit(1)
'''
Esta sessao quebruo a validacao acima. Agora qualquer ip aciona o software.Mesmo se inexistente.
Outra coisa, nao funcionou a validacao por ip somente. Ele aciona a sessao abaixo host ip address.
A primeira while funcionou, mas a segunda quebrou.
'''
while host.isnumeric() and host not in alpha:
    if host.count(".") !=3:
        print ("Invalid IP <---")
        sys.exit(2)
        break

while host.isnumeric() and host not in alpha:
    if host == True:
        break
    print ("\n*******  MAY THE SCAN BEGIN!!!!  *******\n")

if host.isnumeric() and host in alpha:
    print ("\n=============************************************=============")
    print ("*************** The host ip address is: ", socket.gethostbyname(host))
    print ("=============************************************=============\n")

    print ("\n=============************************************=============")
    print ("               Now let me scan the juice out of it!")
    print ("=============************************************=============\n\n")

def port_scan():
    ip = socket.gethostbyname(host)
    list_of_ports = information.chosing_ports()
    print ("\n=============************************************=============")
    print ("\nThe Ports we will scan are: \n", list_of_ports)
    print ("\n=============************************************=============\n\n")

    for port in list_of_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        if (sock.connect_ex ((ip,port)) == 0):
            open_ports.append(port)
            site = requests.get("http://"+host)
            status = site.status_code
            print ("[+] Port ", port, "is OPEN, and the Status is: ", status)
            sock.close()

    return 0

port_scan()

def banner():
    for x in open_ports:
        try:
            mynewsock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
            mynewsock.connect((ip1,x))
            banner = mynewsock.recv(1024)
            mynewsock.close()
            if (x >50):
                print (" ")
            else:
                print ("\n>> For Port number ",x,"The banner is: ",banner,"<---")
        except NameError:
                pass
        except socket.timeout:
                pass
banner()

def parsing():
    if (80 in open_ports):
        print ("\n=============************************************=============")
        print ("           *************** SUBDOMAINS **************          ")
        print ("=============************************************=============\n")

        session = HTMLSession()
        site = session.get("http://"+host)
        parse_r = site.html.links

        for line in parse_r:
            t_line = line.split("/")[-1]
            print (t_line)

parsing()



print ("\n=============************************************=============")
print ("\n\n                        DONE DEAL!\n\n")
print ("=============************************************=============\n\n\n")
