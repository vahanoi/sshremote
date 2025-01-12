'''Started 2020/09/26
remoting via SSH
Questions:
- how to protect credentials cannot store them in plain?
-dependencies list

1 argparse for program arguments
2 netmiko for device access
3 txt list of devices
4 commands to run remotely
5 output export to file


'''
from netmiko import ConnectHandler
import json
import os
import argparse
import getpass

# enter password without display
password = getpass.getpass (prompt="Enter password: ") # getpass.getpass(prompt='Password: ', stream=None)


def main ():
    '''prompt for password to open encrypted device database getpass
    '''
    arguments = argparse.ArgumentParser(description='Execute commands via SSH on the devices.')
    arguments.add_argument ("--test")
    # arguments.add_subparsers ("help")  # for tests
    # create
    with open(devices.txt)
    ssh_host = ['123.123.123.123', 'test','testtest','ls -l']
    # ssh = sshclient(ssh_host)
    # ssh.ssh_session(ssh_host)
    arguments.parse_args()


if __name__ == "__main__":
    # execute only if run as a script
    main()
# help with the programming
# test   