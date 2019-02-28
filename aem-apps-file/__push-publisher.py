import subprocess
import getpass

def push(ip, port, key):
    command = "/usr/src/app/push_publisher.sh " + 'http://' + ip + ':' + port + '/crx/packmgr/service.jsp' + ' ' + key
    subprocess.call(command, shell=True)

if __name__ == "__main__":
    print("AICI2")
    #ip = input("Insert the publisher ip:")
    #port = input("Insert the publisher port:")
    #key = getpass.getpass('Enter the key:')
    ip = '35.183.247.189'
    port = '4503'
    key = 'xvfT9T4FRCWV=W@v?=+Q}GHL'
    push(ip, port, key)
