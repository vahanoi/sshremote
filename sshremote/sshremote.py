'''Started 2020/09/26
remoting via SSH
Questions:
- how to protect credentials cannot store them in plain?

'''
import paramiko  # import SSH2 library
import os

class sshclient:
    '''SSH client class - '''
    def __init__(self,host):  # ssh_host - list: hostname/IP, username, password, command/commands
        self.ssh_client = host

    def ssh_session(self, ssh_host):
        
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=ssh_host[0],
                        username=ssh_host[1],
                        password=ssh_host[2])
        stdin, stdout, stderr = self.ssh_client.exec_command(self.command)
        print(stdout.read().decode().strip())
        print(stderr.read().decode().strip())
        print("Command: "+stdin.read().decode().strip())
        self.ssh_client.close()

def main ():
    ssh_host = ['123.123.123.123', 'test','testtest','ls -l']
    ssh = sshclient(ssh_host)
    ssh.ssh_session(ssh_host)

if __name__ == "__main__":
    # execute only if run as a script
    main()
# help with the programming
# test