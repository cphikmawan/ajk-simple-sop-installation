### Automation SOP AJK Using Ansible

#### Current Requirements
|No|Name|Version|Function|
|---|---|---|---|
|1|Ansible|2.8.4 or latest|Automation tools|
|2|Python|3.6.8 or latest|Running SSH Key Gen script|
|3|SSHPASS|1.06 or latest|Forced using password inline|

#### Will Installed on Future
|No|Name|
|---|---|
|1|Terminator|
|2|Chrome|
|3|VSCode|
|4|Apache2|
|5|MySQL|
|6|VirtualBox|
|7|PHP|
|8|Git|

#### Step 1 - Prepare

##### Prepare File Needed
1. Clone this repository
```sh
$ git clone https://github.com/cphikmawan/automation-sop-ajk-using-ansible
```

2. Rename [hosts.bak](hosts.bak) to __hosts__
```sh
$ mv hosts.bak hosts
```

3. Rename [hosts.json.bak](scripts/hosts.json.bak) with __hosts.json__
```sh
$ mv hosts.json.bak hosts.json
```

##### SSH Key Gen
1. Generate ssh-keygen on master host
```sh
$ ssh-keygen -t rsa
```

2. Copy ssh-key-id to remoted host
```sh
$ ssh-copy-id username@host
```

3. Try to ssh into remoted host
```sh
$ ssh username@host
```

##### SSH Key Gen With Script
If you want automation using script try to run [gen.py](scripts/gen.py)
1. Edit [hosts.json](scripts/hosts.json) with your remoted servers
2. run __gen.py__
```sh
$ python3 gen.py
```
3. Done

#### Step 2 - Configuration & Connection
1. Edit [hosts](hosts) file with remoted server what ever you want, example:
```
[workstation]
10.0.0.1 ansible_user=cloudy ansible_become_pass=secret
```

2. Test connection from master host to remoted host
```sh
$ ansible workstation -m ping
```
3. Success output
```
10.0.0.1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    }, 
    "changed": false, 
    "ping": "pong"
}
```

#### Step 3 - Run The Playbook

1. Run the playbook
```sh
$ ansible-playbook main.yml
```
2. Enjoy :)

Created with <3 By Cloudy