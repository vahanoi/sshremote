'''Started 2020/09/26
remoting via SSH
Questions:
- how to protect credentials cannot store them in plain?

'''
import paramiko  # import SSH2 library
import os

class sshclient:
    
    def __init__(self,command):
        self.ssh_client = sshclient
        self.command = command

    def ssh_session(self, hostname, username, password):
        ssh_host = [hostname, username, password]

        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=ssh_host[1],
                        username='username',
                        password='password')
        stdin, stdout, stderr = self.ssh_client.exec_command(self.command)
        print(stdout.read().decode().strip())
        print(stderr.read().decode().strip())
        self.ssh_client.close()
# help
# test