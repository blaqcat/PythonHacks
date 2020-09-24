import argparse
from scapy.all import *

def findGoogle(pkt):
    if pkt.haslayer(Raw):
        payload = pkt.getlayer(Raw).load
        if 'GET' in payload:
            if 'google' in payload:
    r = re.findall(r'(?i)\&q=(.*?)\&', payload)
    if r:
        search = r[0].split('&')[0]
        search = search.replace('q=', '')