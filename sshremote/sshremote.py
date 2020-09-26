'''Started 2020/09/26
remoting via SSH
'''
import paramiko
import os

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


