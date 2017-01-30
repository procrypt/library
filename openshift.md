Single Master multiple node cluser
Install the packages on host

`sudo yum install -y ansible pyOpenSSL python-cryptography python-lxml`

git clone https://github.com/openshift/openshift-ansible

vim /etc/ansible/hosts
```
# Create an OSEv3 group that contains the masters and nodes groups
[OSEv3:children]
masters
nodes

# Set variables common for all OSEv3 hosts
[OSEv3:vars]
# SSH user, this user should allow ssh based auth without requiring a password
ansible_ssh_user=<user>
ansible_become=true

# If ansible_ssh_user is not root, ansible_sudo must be set to true
ansible_sudo=true

#product_type=openshift
#deployment_type=enterprise (Require RH subscription)
deployment_type=origin

# uncomment the following to enable htpasswd authentication; defaults to DenyAllPasswordIdentityProvider
#openshift_master_identity_providers=[{'name': 'htpasswd_auth', 'login': 'true', 'challenge': 'true', 'kind': 'HTPasswdPasswordIdentityProvider', 'filename': '/etc/openshift/openshift-passwd'}]

# host group for masters
[masters]
<master-ip>

# host group for nodes, includes region info
[nodes]
<master-ip>
<node1-ip>
<node2-ip>
....
<node(n)-ip>
```

Make sure the host system is able to ssh on master and all the nodes.
use `ssh-keygen` and `ssh-copyid`

run the playbook

`ansible-playbook openshift-ansible/playbooks/byo/config.yml`

After finishing the installation open https://<master-ip>:8443, it uses a self-signed certificate and login with user demo:demo
