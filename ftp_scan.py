import ftplib

def anon_login(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anoymous', 'me#your.com')
        print '\n[*] ' + str(hostname) +
            ' FTP Anonymous Logon Succeeded.'
        ftp.quit()
        return True
    except Exception, e:
        print '\n[-] ' + str(hostname) +
             FTP Anonymous Logon Failes.'
        return False
host = '192.168.95.179'
anon_login(host)
