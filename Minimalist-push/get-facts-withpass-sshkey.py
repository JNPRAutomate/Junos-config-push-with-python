from jnpr.junos import Device
from pprint import pprint

NODE='MYROUTER'
user='MYUSER'
ssprivkey='MYSSH_KEY_WITH_PASSWORD'

key_password = getpass('Password for SSH private key file: ')

with Device(host=NODE, user=user, ssh_private_key_file=ssprivkey, passwd=key_password) as dev:
    pprint (dev.facts['hostname'])
    pprint (dev.facts)
dev.close()

