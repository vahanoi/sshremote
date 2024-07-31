import os
from getpass import getpass

from netmiko import ConnectHandler

file_name = "hostdata.txt"
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file_name)

# Open file/s with details for devices
# read list of IPs from file with ios type



# # password prompt
# passwrd = None
# while not passwrd:
#     passwrd = getpass('Password: ')
#     tmp_passwrd = getpass('Repeat password: ')
#     if passwrd != tmp_passwrd:
#         passwrd = None

with open(file_path) as file:
    for line in file:
        if not line.startswith('#'):
            device = line.split()
            print(device)
            router = {"device_type": device[0],
                      "host": device[1]}
            print(router)

# handle connection exceptions
# output type (console, textfile, log entry generate)
# what command has to run

# implement user/password hide method - lib keyring?

# cisco1 = {
#     "device_type": "cisco_ios",
#     "host": "cisco1.lasthop.io",
#     "username": "pyclass",
#     "password": password,
# }


net = ConnectHandler(device_type="linux",
                     host="194.146.24.53",
                     username="root",
                     password=passwrd)
#                     passwrd="oS24YZvfCpCu5anYpwuQ")

output = net.send_command('ls -al')
print(output)
status = net.is_alive()
print(status)
net.disconnect()

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
