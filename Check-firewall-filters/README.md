Check if the pushed Firewall Filters do match any traffics.

This python script just queries the Junos device to catch specific firewall filter name (precisely aiming at checking the other script to push a config) and display counters comming from this.

Usage: python3 check-firewall-filter-on-any-router.py


laurent@linux:~/TDD$ python3 check-firewall-filter-on-any-router.py --help
Usage: check-firewall-filter-on-any-router.py [-h] [-r TARGET] [-u LOGIN] [-p PASSWD] [-f FILTER]
optional arguments:
  -h, --help            show this help message and exit
  -r TARGET, --router TARGET
                        router name or IP
  -u LOGIN, --user LOGIN
                        user name to login
  -p PASSWD, --password PASSWD
                        password to use
  -f FILTER, --filter FILTER
                        filter name, default is CORERO-MITIGATE


If any traffics matching this filter, it will display:


laurent@linux:~/TDD$ python3 check-firewall-filter-on-any-router.py
--------------------------------------------------------------------------
Checking a firewall filter counter on a router using show (in xml format)
--------------------------------------------------------------------------
   => target=mx01	 login=MYLOGIN	 pass=******************
   => filter=CORERO-MITIGATE
-------------------------------------------------------------------------------
Summary: counter_name=Corero-Allowed	packet_count=588785898	byte_count=607341797505
Summary: counter_name=Corero-auto-ping-ipv4-1-discard	packet_count=16035902	byte_count=16484907256
Summary: counter_name=Corero-auto-ping-ipv4-1-match	packet_count=16035902	byte_count=16484907256


