# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  # Forward keys from SSH agent rather than copypasta
  config.ssh.forward_agent = true

  # Allow for irc clients on host to connect via localhost:6666
  config.vm.network "forwarded_port", guest: 6667, host: 6666

  config.vm.provision :ansible do |ansible|
    ansible.galaxy_role_file = 'requirements.yml'
    ansible.playbook = "playbook.yml"
    ansible.groups = {
      "vagrant" => ['default'],
    }
  end
end
