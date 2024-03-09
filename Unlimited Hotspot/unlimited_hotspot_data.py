import os
import time
command1 = "C:/Windows/System32/netsh.exe int ipv4 set glob defaultcurhoplimit=65"
command2 = "C:/Windows/System32/netsh.exe int ipv6 set glob defaultcurhoplimit=65"

os.system(command1)
print("IPV4 configuration set successfully!\n")
time.sleep(0.2)
os.system(command2)
print("IPV6 configuration set successfully!\n")

input("Press enter to exit..")

