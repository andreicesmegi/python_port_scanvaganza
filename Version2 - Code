!/bin/python3
import sys
import socket
import information
import requests
from requests_html import HTMLSession

print ("\n\n\n=============****   PYTHON PORT SCANVAGANZA  ****=============")
print ("=============****           VERSION 2        ****=============")
print ("=============****                            ****=============")
print ("=============****  INSERT YOUR HOST AND WAIT ****=============")
print ("=============****                            ****=============")
print ("=============************************************=============\n")

host = input("\n Please, insert the host name ---> ")
ip1 = socket.gethostbyname(host)

open_ports = []

print ("\n=============************************************=============")
print ("*************** The host ip address is: ", ip1)
print ("=============************************************=============\n")

print ("\n=============************************************=============")
print ("               Now let me scan the juice out of it!")
print ("=============************************************=============\n\n")

def port_scan():
    ip = ip1
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

            print (line)
parsing()



print ("\n=============************************************=============")
print ("\n\n                        DONE DEAL!\n\n")
print ("=============************************************=============\n\n\n")
