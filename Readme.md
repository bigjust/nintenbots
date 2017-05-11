Getting Started
---------------

Ansible and Vagrant are required.

```
vagrant up
```

Now we have a running xela kebert on a local irc server. A simple
tweak of a couple ansible variables, and this can be deployed to a
remote server, using a real irc network.

```
ansible-playbook -i <path/to/inventory_file> playbook.yml
```
