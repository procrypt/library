###oc cluster up without insecure registry.

`oc --skip-registry-check=true cluster up`

###Add user to docker group to docker run without sudo.

`sudo gpasswd -a <user> docker`

###Byoubu split terminals.

`shift + F2` Horizontal

`ctrl + F2` Vertical

###Differece between `set +e` and `set -e`

`set -e` sets an non-ignoring error state.That means, if command or pipeline has an error (something returns non zero), the bash will stop the execution of the script.
`set +e` sets error ignoring state

###To fix ssh-key-error-permission-denied-publickey-gssapi-keyex-gssapi-with-mic

```
vim /etc/sshd_config
#PasswordAuthentication no
```

###OpenShift online developer preview

Login to https://console.preview.openshift.com/console/

Get the access token https://api.preview.openshift.com/oauth/token/request

Install `oc client` from https://github.com/openshift/origin/blob/master/docs/cluster_up_down.md#linux

`oc login --token=xxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx --server=https://api.preview.openshift.com`

###Run container in OpenShift with root access

```
   oc login -u system:admin
   oc edit scc restricted
```
Change the `runAsUser` strategy to `RunAsAny`.

