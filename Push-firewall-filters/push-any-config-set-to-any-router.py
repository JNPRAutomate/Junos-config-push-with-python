#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.utils.config import Config
import re
import sys
import argparse

router   = 'MYROUTERIPORNAME'
user     = 'MYUSER'
password = 'MYPASS'
filename = 'SOMEDEFAULTCONFIG'

parser = argparse.ArgumentParser(description='Push some ephemeral config via netconf to a router')
parser.add_argument('-r', '--router',      dest="target",      default=router,   help='router name or IP')
parser.add_argument('-u', '--user',        dest='login',       default=user,     help='user name to login')
parser.add_argument('-p', '--password',    dest='passwd',      default=password, help='password to use')
parser.add_argument('-f', '--filter',      dest='file',        default=filename, help='file containing the filters to push to the router')
parser.add_argument('-m', '--format',      dest='format',      default='set',    help='format of config to be send: set (default), text (junos), xml, json')
parser.add_argument('-e', '--ephemeral',   dest='ephemeral',   default=True,     help='if ephemeraldb is used (default: True)')
parser.add_argument('-e', '--ephemeraldb', dest='ephemeraldb', default="Corero", help='the ephemeraldb name to use (default: Corero)')
args = parser.parse_args()
target = args.target
login  = args.login
passwd = args.passwd
file   = args.file
format = args.format
ephemeral = args.ephemeral
ephemeraldb = args.ephemeraldb

#print(" target=%s\n login=%s\n pass=%s\n file=%s\n" % (target,login,passwd,file))
print("-------------------------------------------------------------------------------")
print("Pushing a config to a router using ephemeraldb instance (config in set format) ")
print("-------------------------------------------------------------------------------")
print("   => target=%s\t login=%s\t pass=******************" % (target,login))
print("   => format=%s\t file=%s\n" % (format,file))

dev = Device(host=target, user=login, password=passwd)
try:
    dev.open()
    if ephemeral==True:
        print("Using ephemeraldb instance %s " %(ephemeral) with database %(ephemeraldb))
        with Config(dev, mode='ephemeral', ephemeral_instance=ephemeraldb) as cu:
             cu.load(path=file, format=format, merge=True)
             cu.commit(force_sync=True)
    else:
        print("Not using ephemeraldb instance, then pushing the new config to main config (and merge it)")
        with Config(dev) as cu:
             cu.load(path=file, format=format, merge=True)
             cu.commit(force_sync=True)
    print ("pushed the config to the router")
    dev.close()

except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
print("-------------------------------------------------------------------------------")

