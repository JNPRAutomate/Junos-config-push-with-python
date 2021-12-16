from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.utils.config import Config
from pprint import pprint
from lxml.builder import E

router='MYROUTER'
user='MYUSER'
password='MYPASS'

dev = Device(host=router, user=user, password=password)
try:
    dev.open()
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)

with Config(dev, mode='ephemeral', ephemeral_instance='Corero') as cu:
    cu.load(path='ff-delete.conf', format='set', merge=True)
    cu.commit(force_sync=True)

dev.close()

