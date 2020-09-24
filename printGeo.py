import dpkt
import socket
import pygeoip
import argparse

gi =pygeoip.GeoIP('/home/panther/Downloads/GeoLite2-City_20200915/GeoLite2-City.mmdb')

def retGeoStr(ip):
    try:
        rec= gi.record_by_name(ip)
        city =rec['city']
        country = rec['country_code3']
        if city != '':
            geoLoc = city + ',' + country
        else:
            geoLoc = country
        return geoLoc
    except Exception as e:
        return 'Unregistered'
def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print '[+] Src: ' + src + '--> Dst: ' + dst
            print '[+] Src: ' + retGeoStr(src) + ' --> Dst: ' + retGeoStr()
        except:
            pass

def main():
    parser = argparse.ArgumentParser('-p <pcap file>')
    parser.add_argument('-p', dest='pcapFile', type=str, help='specify pcap filename')
    args = parser.parse_args()
    if args.pcapFile == None:
        print parser.usage
        exit(0)
        pcap = args.pcapFile
        printPcap(pcap)

if __name__ == '__main__':
    main()
