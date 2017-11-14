# IP check

Slack bot that allows users to lookup the ip addresses of systems that don't allow hostnames

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
pip install slackclient
pip install netifaces
```


### Installing

rename config_example.py to config.py and fill it in with the details. Be sure not to accidentally push the slack key to a public repo. In ip-check.service change the ubuntu user to who you want the bot to run as. Fill in the paths to the script and log files.


```
sudo cp ip-check.service /lib/systemd/system/ip-check.service
sudo chmod 644 /lib/systemd/system/ip-check.service
sudo systemctl daemon-reload
sudo systemctl enable ip-check.service
```
