# Junos-config-push
Push any config to any Junos in various formats: set (default), text (hierarchical Junos config), xml or json

This script was written to try ephemeraldb usage on MX with TDD (Corero partnership) as this anti-DDoS tool will generate dynamically Firewall Filters and push them to the MX using Ephemeraldb (temp config that does not stay in the main config) via Netconf/SSH.
I then used this to try many syntax of those kind of scripts to find the limits and possibilities, also on various platforms.
I then made a more generic script over time to be able to push almost any config to any Junos device with or without Ephemeraldb config.
I added a few sample firewall filters that can be loaded in text/junos, set/delete formats.



linux$ **python3 push-any-config-set-to-any-router.py --help**
```
usage: push-any-config-set-to-any-router.py [-h] [-r TARGET] [-u LOGIN] [-p PASSWD] [-f FILE] [-m FORMAT] [-e EPHEMERAL]

Push some ephemeral config via netconf to a router

optional arguments:
  -h, --help            show this help message and exit
  -r TARGET, --router TARGET
                        router name or IP
  -u LOGIN, --user LOGIN
                        user name to login
  -p PASSWD, --password PASSWD
                        password to use
  -f FILE, --filter FILE
                        file containing the filters to push to the router
  -m FORMAT, --format FORMAT
                        format of config to be send: set (default), text (junos), xml, json
  -e EPHEMERAL, --ephemeral EPHEMERAL
                        if ephemeraldb is used (default: True)_

```


Example with a junos formatted config (using 'text' syntax as per netconf uses) and it's set format counterpart:

This part adds the filter to the router:
laurent@linux:~/TDD$ python3 push-any-config-set-to-any-router.py -f firewallfilter-dns-attack.conf -m text
```
-------------------------------------------------------------------------------
Pushing a config to a router using ephemeraldb instance (config in set format)
-------------------------------------------------------------------------------
   => target=mx01	 login=admin	 pass=******************
   => format=text	 file=firewallfilter-dns-attack.conf

Using ephemeraldb instance True
pushed the config to the router
```


Showing the effect on the router:

laurent@mx01_re0> show ephemeral-configuration instance Corero
```## Last changed: 2021-12-13 09:01:25 PST
firewall {
    family inet {
        filter CORERO-MITIGATE {
            term egress_manual {
                then next term;
            }
            term discard_manual {
                then next term;
            }
            term discard_auto {
                then next term;
            }
            term accept_manual {
                then next term;
            }
            term accept_auto {
                then next term;
            }
            term dns-attack-match {
                from {
                    destination-address {
                        10.10.13.2/32;
                    }
                    packet-length-except 1-77;
                    protocol udp;
                    source-port 53;
                    flexible-match-mask {
                        match-start layer-4;
                        byte-offset 53;
                        bit-offset 0;
                        bit-length 32;
                        mask-in-hex 0xffffffff;
                        prefix 0x0000ff00;
                    }
                }
                then {
                    count Corero-auto-dns-attack-match;
                    port-mirror;
                    next term;
                }
            }
            term dns-attack-action {
                from {
                    destination-address {
                        10.10.13.2/32;
                    }
                    packet-length-except 1-77;
                    protocol udp;
                    source-port 53;
                    flexible-match-mask {
                        match-start layer-4;
                        byte-offset 53;
                        bit-offset 0;
                        bit-length 32;
                        mask-in-hex 0xffffffff;
                        prefix 0x0000ff00;
                    }
                }
                then {
                    count Corero-auto-dns-attack-discard;
                    discard;
                }
            }
        }
    }
}
```


This part deletes the added filter to the router:

laurent@linux:~/TDD$ python3 push-any-config-set-to-any-router.py -f firewallfilter-dns-attack-delete.conf
```-------------------------------------------------------------------------------
Pushing a config to a router using ephemeraldb instance (config in set format)
-------------------------------------------------------------------------------
   => target=mx01	 login=admin	 pass=******************
   => format=set	 file=firewallfilter-dns-attack-delete.conf

Using ephemeraldb instance True
pushed the config to the router
-------------------------------------------------------------------------------
```

laurent@mx01_re0> show ephemeral-configuration instance Corero
```## Last changed: 2021-12-13 09:02:08 PST
firewall {
    family inet {
        filter CORERO-MITIGATE {
            term egress_manual {
                then next term;
            }
            term discard_manual {
                then next term;
            }
            term discard_auto {
                then next term;
            }
            term accept_manual {
                then next term;
            }
            term accept_auto {
                then next term;
            }
        }
    }
}
```
(Here some filters are left on purpose)
