import re
import argparse
from scapy import *

def findCreditCard(pkt):
    raw = pkt.sprintf('%Raw.load%')
    americaRE = re.findall('3[47][0-9]|13|', raw)
    masterRE = re.findall('5[1-5][0-9]|14|', raw)
    visaRE = re.findall('4[0-9]|12|(?:[0-9]|3|)?', raw)
    if americaRE:
        print '[+] Found American Express Card: ' + amricaRE[0]
    if masterRE:
        print '[+] Found MasterCard Card: ' + masterRE[0]
    if visaRE:
        print '[+] Found Visa Card: ' + visaRE[0]

def main():
    parser = argparse.ArgumentParser('%prog -i<interface>')
    parser.add_argument('-i', dest='interface', type=str, help='specify interface to isten on')
    args = parser.parse_args()
    if args.interface == None:
        print parser.usage
        exit(0)

if __name__ == '__main__':
    main()