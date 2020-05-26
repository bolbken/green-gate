# green-gate
Scripts and files to create a minimum admin server on a Raspberry Pi or other low-power usage device that can power on and off servers in a home intended for remote access.

## Installation
1. On a fresh install of Ubuntu or Raspbian with users setup as required and internet connection run the following in a terminal.

```bash
sudo apt update && sudo apt upgrade
```

2. Install the following packages as pre-requisits for the following steps.

```bash
sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent \
  software-properties-common libffi-dev libssl-dev 
```

3. Install python 3.8 using the ppa.

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
```

4. Install docker and add your service account `user_name` to the docker group.

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker [user_name]
```

**IMPORTANT**: _Reboot the machine after this step._

5. Install docker compose

```bash
sudo apt install -y python3 python3-pip
sudo pip3 install docker-compose
```

6. 


## Start the development server

```bash
export FLASK_APP=./green_gate/api/__init__.py && flask run
```


## Start the production server

```bash
gunicorn --bind 0.0.0.0:5000 green_gate.api.server:app
```