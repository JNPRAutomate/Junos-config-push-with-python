#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.utils.config import Config
from jnpr.junos.factory.factory_loader import FactoryLoader
import re
import sys
import argparse
import json
import yaml
import yamlordereddictloader
from pprint import pprint
from lxml import etree
import jxmlease

router   = 'MYROUTERIPORNAME'
user     = 'MYUSER'
password = 'MYPASS'
filtername = 'CORERO-MITIGATE'

parser = argparse.ArgumentParser(description='Push some ephemeral config via netconf to a router')
parser.add_argument('-r', '--router',   dest="target", default=router,     help='router name or IP')
parser.add_argument('-u', '--user',     dest='login',  default=user,       help='user name to login')
parser.add_argument('-p', '--password', dest='passwd', default=password,   help='password to use')
parser.add_argument('-f', '--filter',   dest='filter', default=filtername, help='filter name, default is CORERO-MITIGATE')
args = parser.parse_args()
target = args.target
login  = args.login
passwd = args.passwd
filter = args.filter

print("--------------------------------------------------------------------------")
print("Checking a firewall filter counter on a router using show (in xml format) ")
print("--------------------------------------------------------------------------")
print("   => target=%s\t login=%s\t pass=******************" % (target,login))
print("   => filter=%s" % (filter))
print("-------------------------------------------------------------------------------")

# SHOW COMMAND:
# laurent@mx01> show firewall filter CORERO-MITIGATE |display xml rpc
#<rpc-reply xmlns:junos="http://xml.juniper.net/junos/19.4R0/junos">
#    <rpc>
#        <get-firewall-filter-information>
#                <filtername>CORERO-MITIGATE</filtername>
#        </get-firewall-filter-information>
#    </rpc>
#    <cli>
#        <banner></banner>
#    </cli>
#</rpc-reply>
# 
# RESULT:
# laurent@mx01> show firewall filter CORERO-MITIGATE |display xml
#<rpc-reply xmlns:junos="http://xml.juniper.net/junos/19.4R0/junos">
#    <firewall-information xmlns="http://xml.juniper.net/junos/19.4R0/junos-filter">
#        <filter-information>
#            <filter-name>CORERO-MITIGATE</filter-name>
#            <counter>
#                <counter-name>Corero-Allowed</counter-name>
#                <packet-count>416316713</packet-count>
#                <byte-count>274462490908</byte-count>
#            </counter>
#            <counter>
#                <counter-name>Corero-auto-customfilter0000-discard</counter-name>
#                <packet-count>0</packet-count>
#                <byte-count>0</byte-count>
#            </counter>
#            <counter>
#                <counter-name>Corero-auto-customfilter0000-match</counter-name>
#                <packet-count>0</packet-count>
#                <byte-count>0</byte-count>
#            </counter>
#        </filter-information>
#    </firewall-information>
#    <cli>
#        <banner></banner>
#    </cli>
#</rpc-reply>

print("\n---------------------------  BEGIN  -----------------------------------")
try:
    with Device(host=target, user=user, password=password) as dev:
         firewallfilters_rpc = dev.rpc.get_firewall_filter_information(filtername=filter)
    dev.close()
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))

print("\n-------------------------  XML TO JSON  -------------------------------")
firewallfilters_xml = etree.tostring(firewallfilters_rpc, pretty_print=True, encoding='unicode')
result = jxmlease.parse(firewallfilters_xml)

print("\n--------------------------  DECODE JSON  ------------------------------")
if 'counter' in result['firewall-information']['filter-information']:
    counters = result['firewall-information']['filter-information']['counter']

    if 'counter-name' in result['firewall-information']['filter-information']['counter']:
         counter_name = counters['counter-name']
         packet_count = counters['packet-count']
         byte_count   = counters['byte-count']
         print("Summary: counter_name=" + str(counter_name) + '\tpacket_count=' + packet_count + \
               '\tbyte_count=' + byte_count)

    else:
         for counter in counters:
             counter_name = counter['counter-name']
             packet_count = counter['packet-count']
             byte_count   = counter['byte-count']
             print("Summary: counter_name=" + str(counter_name) + '\tpacket_count=' + packet_count + '\tbyte_count=' + byte_count)

else:
    print("No counter exists for that filter")

print("\n---------------------------  END  -------------------------------------\n")

