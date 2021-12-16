# Junos-config-push-with-python

The need to push config to any Junos in various formats is nice for scripting and many the possible reasons.
Also the need to push other commands, not only config, come later when trying to get various status, statistics or debugs.


Those scripts were written to try to deal with config on various platforms, mainly MX initially, to use ephemeraldb on MX with TDD (Corero partnership) as this anti-DDoS tool will generate dynamically Firewall Filters and push this those to the MX using Ephemeraldb (temporarily config that does not stay in the main config but is used by the Trio chipset) via Netconf/SSH.

I then used this to try many syntax of those kind of scripts to find the limits and possibilities, also on various platforms.
I could then try which other platforms could be allowed to be used with TDD (but not only as others may use also ephemeraldb).


# Minimalist-push:
This contains some basic push commands using either a user/pass or ssh keys.


# Push-firewall-filters:
This contains more advanced script to do the same but in a more generic way.
I made this generic script to be able to push almost any config to any Junos device with or without Ephemeraldb config (this can be MX, SRX, PTX, etc...).
I added a few sample firewall filters that can be loaded in text/junos, set/delete formats.

Configs can be of form: set (default), text (hierarchical Junos config), xml or json
to get the config we need, it can be done with:
- native Junos config:    show configuration
- set format:             show configuration | display set
- xml format:             show configuration | display xml
- json format:            show configuration | display json


# Check-firewall-filters:
This contains a script to get the output of above Firewall Filters counters (set either via above or any other method).
This is used in a larger script to check whether a series of filters do match after applying (from a library of attacks, I may share that sometimes but it's a bit more complex to detail).


I have other scripts to be added here too... Stay tuned.
Laurent
