# Junos-config-push

The need to push config to any Junos in various formats is nice for scripting and all the possible reasons.

Those scripts were written to try to deal with config on various platforms, mainly MX initially, to use ephemeraldb on MX with TDD (Corero partnership) as this anti-DDoS tool will generate dynamically Firewall Filters and push this those to the MX using Ephemeraldb (temporarily config that does not stay in the main config but is used by the Trio chipset) via Netconf/SSH.

I then used this to try many syntax of those kind of scripts to find the limits and possibilities, also on various platforms.
I could then try which other platforms could be allowed to be used with TDD (but not only).

I then made a more generic script over time to be able to push almost any config to any Junos device with or without Ephemeraldb config.
I added a few sample firewall filters that can be loaded in text/junos, set/delete formats.

Configs can be of form: set (default), text (hierarchical Junos config), xml or json
to get the config we need, it can be done with:
- native Junos config:    show configuration 
- set format:             show configuration | display set
- xml format:             show configuration | display xml
- json format:            show configuration | display json

I added other scripts to be added here too... Stay tuned.
Laurent
