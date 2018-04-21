### oc cluster up without insecure registry.

`oc --skip-registry-check=true cluster up`

### oc bash completion
`source <(oc completion bash)`

### Add user to docker group to docker run without sudo.

`sudo gpasswd -a $(whoami) docker`

Update your current session for the group change to take effect

`newgrp docker`

or

`sudo usermod -aG docker $(whoami)`

`newgrp docker`

### Run docker with insecure registry
`vim /usr/lib/systemd/system/docker.service`

Add the registry this line 
`ExecStart=/usr/bin/dockerd`

eg: `ExecStart=/usr/bin/dockerd --insecure-registry docker-registry.usersys.redhat.com --insecure-registry 172.30.0.0/16`

```
sudo systemctl daemon-reload
sudo systemctl restart docker
```

### MiniShift Installation
```
wget https://github.com/minishift/minishift/releases/download/v1.0.0/minishift-1.0.0-linux-amd64.tgz
tar -zxvf minishift-1.0.0-linux-amd64.tgz
mv minishift /usr/local/bin/
```
#### Install KVM
```
sudo curl -L https://github.com/dhiltgen/docker-machine-kvm/releases/download/v0.7.0/docker-machine-driver-kvm -o /usr/local/bin/docker-machine-driver-kvm
sudo chmod +x /usr/local/bin/docker-machine-driver-kvm
```
#### Start MiniShift
`minishift start`

### Byoubu split terminals.

`shift + F2` Horizontal

`ctrl + F2` Vertical

`shift + F11` Maximize the window

`ctrl + shift + F4` Swap Sessions

`ctrl + F6` Forcefully kill a pane


### Differece between `set +e` and `set -e`

`set -e` sets an non-ignoring error state.That means, if command or pipeline has an error (something returns non zero), the bash will stop the execution of the script.
`set +e` sets error ignoring state

### To fix ssh-key-error-permission-denied-publickey-gssapi-keyex-gssapi-with-mic

```
vim /etc/ssh/sshd_config
#PasswordAuthentication no
```

### OpenShift online developer preview

Login to https://console.preview.openshift.com/console/

Get the access token https://api.preview.openshift.com/oauth/token/request

Install `oc client` from https://github.com/openshift/origin/releases

`oc login --token=xxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx --server=https://api.preview.openshift.com`

### Run container in OpenShift with root access

```
   oc login -u system:admin
   oc edit scc restricted
```
Change the `runAsUser.Type` strategy to `RunAsAny`.


### Add this to your bashrc to avoid branching errors in git

```
git clone https://github.com/magicmonty/bash-git-prompt.git .bash-git-prompt
echo 'source ~/.bash-git-prompt/gitprompt.sh' >> ~/.bashrc
echo 'GIT_PROMPT_ONLY_IN_REPO=1' >> ~/.bashrc
```

### Export TERM in Linux
`export TERM=xterm`

### Download youtube videos in best quality
`youtube-dl -f bestvideo+bestaudio <url>`

### Openshift insecure_registry patch

`oc patch is $imagestream -p '{"metadata":{"annotations":{"openshift.io/image.insecureRepository": "true"}}}}'`
`oc import-image $imagestream:<tag>`

### Thinkpad vimrc
```bash
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
[ -r /home/abhishek/.byobu/prompt ] && . /home/abhishek/.byobu/prompt   #byobu-prompt#
export PATH=$PATH:/usr/local/go/bin
export GOPATH=$HOME/work/golang
export PATH=$PATH:/home/abhishek/work/golang/bin
export CDPATH=$HOME/work/golang/src/github.com/
export GOOGLE_APPLICATION_CREDENTIALS=$PATH:/home/abhishek/
source ~/.bash-git-prompt/gitprompt.sh
GIT_PROMPT_ONLY_IN_REPO=1
export EDITOR=/usr/bin/vim
export VAGRANT_DEFAULT_PROVIDER=libvirt
export PS1="\e[0;36m\]🕸 \e[0;31m\]procrypt \e[0;32m\]\W \e[00m\]$ \e[m";
source <(kubectl completion bash)
source <(kompose completion bash)

# The next line updates PATH for the Google Cloud SDK.
if [ -f /home/abhishek/Downloads/google-cloud-sdk/path.bash.inc ]; then
  source '/home/abhishek/Downloads/google-cloud-sdk/path.bash.inc'
fi

# The next line enables shell command completion for gcloud.
if [ -f /home/abhishek/Downloads/google-cloud-sdk/completion.bash.inc ]; then
  source '/home/abhishek/Downloads/google-cloud-sdk/completion.bash.inc'
fi
```

### Bash Propmt
`PS1="\[\e[0;36m\]🕸 \[\e[0;31m\]procrypt \[\e[0;32m\]\W \[\e[00m\]\@ $ \[\e[m";` // With Time

`PS1="\[\e[0;36m\]🕸  \[\e[0;31m\]procrypt \[\e[0;32m\]\W \[\e[00m\]$ \[\e[m";`  


Byobu
```
\[\e[31m\]$(byobu_prompt_status)\[\e[00;32m\]\u\[\e[00m\]@\[\e[00;31m\]\h\[\e[00m\]:\[\e[00;36m\]\w\[\e[00m\]$(byobu_prompt_symbol)
```

### Install Go 
```
$ wget -P go$VERSION.$OS-$ARCH.tar.gz
$ tar -C /usr/local -xzf /tmp/go$VERSION.$OS-$ARCH.tar.gz
$ export PATH=$PATH:/usr/local/go/bin 
$ export GOROOT=$HOME/go
```

### Update Go 
```
$ rm -rf /usr/local/go
```
Repeat the above steps

### Golang best practices
https://talks.golang.org/2013/bestpractices.slide#1

https://peter.bourgon.org/go-best-practices-2016/

https://medium.com/@sebdah/go-best-practices-error-handling-2d15e1f0c5ee


Golang best practices

https://talks.golang.org/2013/bestpractices.slide#1

https://peter.bourgon.org/go-best-practices-2016/

https://medium.com/@sebdah/go-best-practices-error-handling-2d15e1f0c5ee

https://golang.org/doc/effective_go.html

Cool thing :)

`curl http://wttr.in/~Jaipur`
