"""
Created on Sat Mar 27

@author: ktk
"""
import socket
from Functions import sub
def ipaddress():
    hostname = socket.gethostname()   
    IPAddr = socket.gethostbyname(hostname)   
    return (f"Your IP address is {IPAddr}")
