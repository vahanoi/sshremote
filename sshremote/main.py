import os
import sys
from getpass import getpass
from netmiko import ConnectHandler,exceptions
import argparse

# argparser here for com

file_name = "hostdata.txt" # can be specified in start path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file_name)

#
# startup parser for filename, command file, output filename
# sshremote.py -f device_list -c commands -o output
# Open file/s with details for devices
# read list of IPs from file with ios type
# identify device type: cisco_ios, cisco_xe, cisco_nxos....
# analise data
#


# cisco1 = {
#     "device_type": "cisco_ios",
#     "host": "cisco1.lasthop.io",
#     "username": "pyclass",
#     "password": password,
# }

pass1=getpass(prompt="Password: ")
#secret=getpass(prompt="Enter Enable secret: ")

#
# router file access - for list of routers
#

try:
    with open(file_path) as file:
        for line in file: # for each line in the file - main loop
            if not (line.startswith('#') or line=="\n"):   # if line not starting from comment or empty                               
                device = line.split()
                router = {"device_type": device[0],
                        "host": device[1]}
                print(router)
                device_data = {
                                "device_type" : device[0],
                                "host" : device[1],
                                "username" : "marcin", # username 
                                "password" : pass1,
                                "global_delay_factor": 2
                                }
# Connect to the device                 
                try:
                    device = ConnectHandler (**device_data)
                    if not device.find_prompt().endswith('#'):      # verify if in Enable mode
                        secret=getpass(prompt="Enable password: ")  # if not ask for pass
                        device.enable()                             # execute enable
                    device.clear_buffer
#                    print(isEnable)
#                    device.enable()
# execute command on device
                    output = device.send_command('show runn | i username admin|username Admin|username ADMIN')
                    print("=========== "+device_data["host"]+" ===========\n\n")
                    print(output)
                    device.disconnect()
                except exceptions.NetmikoTimeoutException:
                    print("Timeout connecting to ",device_data["host"])
                except exceptions.NetmikoAuthenticationException:
                    print("Authentication Error connecting to ",device_data["host"])
                except exceptions.ConnectionException:
                    print("Cant connect to ",device_data["host"])
# summary at the end 
except OSError:
    print ("Could not find a file ", file_path), 
    sys.exit (1)

# handle connection exceptions
# output type (console, textfile, log entry generate)
# what command has to run

# implement user/password hide method - lib keyring?

'''
 def main ():
    None

if __name__ == "__main__":
    # execute only if run as a script
    main()


# read ip and user/pass from file
# find the original script for cisco and update with netmiko
# list of devices from excel/text/csv
'''
