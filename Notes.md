###oc cluster up without insecure registry.

`oc --skip-registry-check=true cluster up`

###Add user to docker group to docker run without sudo.

`sudo gpasswd -a <user> docker`

or

`sudo usermod -aG docker $(whoami)`

###Run docker with insecure registry
`vim /usr/lib/systemd/system/docker.service`

Add the registry this line 
`ExecStart=/usr/bin/dockerd`

eg: `ExecStart=/usr/bin/dockerd --insecure-registry docker-registry.usersys.redhat.com --insecure-registry 172.30.0.0/16`

```
sudo systemctl daemon-reload
sudo systemctl restart docker
```

###Byoubu split terminals.

`shift + F2` Horizontal

`ctrl + F2` Vertical

`shift + F11` Maximize the window

`ctrl + shift + F4` Swap Sessions


###Differece between `set +e` and `set -e`

`set -e` sets an non-ignoring error state.That means, if command or pipeline has an error (something returns non zero), the bash will stop the execution of the script.
`set +e` sets error ignoring state

###To fix ssh-key-error-permission-denied-publickey-gssapi-keyex-gssapi-with-mic

```
vim /etc/ssh/sshd_config
#PasswordAuthentication no
```

###OpenShift online developer preview

Login to https://console.preview.openshift.com/console/

Get the access token https://api.preview.openshift.com/oauth/token/request

Install `oc client` from https://github.com/openshift/origin/releases

`oc login --token=xxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx --server=https://api.preview.openshift.com`

###Run container in OpenShift with root access

```
   oc login -u system:admin
   oc edit scc restricted
```
Change the `runAsUser` strategy to `RunAsAny`.


###Add this to your bashrc to avoid branching errors in git

```
git clone https://github.com/magicmonty/bash-git-prompt.git .bash-git-prompt
echo 'source ~/.bash-git-prompt/gitprompt.sh' >> ~/.bashrc
echo 'GIT_PROMPT_ONLY_IN_REPO=1' >> ~/.bashrc
```

###Export TERM in Linux
`export TERM=xterm`

###Download youtube videos in best quality
`youtube-dl -f bestvideo+bestaudio <url>`

Openshift insecure_registry patch
`oc patch is $imagestream -p '{"metadata":{"annotations":{"openshift.io/image.insecureRepository": "true"}}}}'`
`oc import-image $imagestream:<tag>`
