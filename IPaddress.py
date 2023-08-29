"""
Created on Sat Mar 27

@author: ktk
"""
import socket
from Functions import sub
def ipaddress():
    hostname = socket.gethostname()   
    IPAddr = socket.gethostbyname(hostname)   
    sub(f"Your Computer Name is: {hostname}")   
    sub(f"Your Computer IP Address is: {IPAddr}")