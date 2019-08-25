import json
import subprocess
import os.path

# read file
def readFile():
    with open('hosts.json', 'r') as host:
        data=host.read()
    # parse file
    values = json.loads(data)
    return values

# check existing key
def checkExistingKey():
    check = os.path.isfile('/home/cloudy/.ssh/id_rsa')
    return check

# main
def main():
    values = readFile()
    check = checkExistingKey()
    
    if check:
        for value in values:
            command = "sshpass -p %s ssh-copy-id -o StrictHostKeyChecking=no -p %s %s@%s" % (value['pass'], value['port'], value['username'], value['host'])
            print(command)
            subprocess.call(command, shell=True)
    else:
        subprocess.run(["ssh-keygen", "-t", "rsa"])

if __name__ == "__main__":
    main()


# Create by Cloudy