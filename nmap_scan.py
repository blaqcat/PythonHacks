#Nmap Scanner

import nmap
import argparse

def nmapSCan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print " [*] " + tgtHost + " tcp/"+tgtPort +" "+state

def main():
    parser = argparse.ArgumentParser('usage%prog ' +
                        ' -H <target host> -p <target port>')
    parser.add_argument('-H', dest='tgtHost', type=str,
                        help='specify target host')
    parser.add_argument('-p', dest='tgtPort', type=str,
                        help='specify target port[s] separated by comma')
    args = parser.parse_args()
    tgtHost = args.tgtHost
    tgtPorts = str(args.tgtPort).split(', ')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print parser.usage
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':
    main()
