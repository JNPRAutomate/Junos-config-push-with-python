from jnpr.junos import Device
from pprint import pprint

NODE='MYROUTER'
user='MYUSER'
ssprivkey='MYSSH_KEY_WITHOUT_PASSWORD'

with Device(host=NODE, user=user, ssh_private_key_file=ssprivkey) as dev:
    pprint (dev.facts['hostname'])
    pprint (dev.facts)
dev.close()

