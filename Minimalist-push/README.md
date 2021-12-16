# Minimalist push configs to a Junos device using a user/password or using a ssh key.

Those script just show how to basically interact with the config using either simple login/password or also ssh keys with or without password.


Simple login, push config:

**junos-filters-push.py**:  pushes a ff.conf junos config

**junos-filters-delete.py**: pushes the matching junos delete in set format


SSH keys login, get facts:

**get-facts-nopass-sshkey.py**: get informations on junos device using no password ssh key

**get-facts-withpass-sshkey.py**: get informations on junos device using a password protected ssh key (prompt for password)

