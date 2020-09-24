
from geolite2 import geolite2
import json
file_name = 'home/blackpanther/test.pcap/'
reader = geolite2.filename(file_name)

print json.dumps(reader['continent']['names']['en'], indent=4)
print json.dumps(reader['country']['names']['en'], indent=4)
print json.dumps(reader['location']['latitude'], indent=4)
print json.dumps(reader['location']['longitude'], indent=4)
