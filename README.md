# home-server
 Use raspberri pi 4 to build a home server while working. 

## Decide which system to use.
 Either Ubuntu 21.10 desktop or server.

## Install on SSD or SD card using Raspberry Pi Imager.
 https://www.raspberrypi.com/software/

 Note: When a SD card is inserted the default boot mode will boot from the card instead from USB.
 If no card is inserted the system will boot directly from USB. (You could change it manually.)

## Connect to the internet first time
 Lan:
 WIFI:

## Add default user and password
 User: ubuntu
 Password: ####


## Connect via SSH
 First-time use ssh user@192.168.2.120 (or whatever your IP is, you can check in router listings.)

 After:
 Create ssh public on default machine.
 Move public key "scp {key_pub} user@ip:/home/{username}" to server.
 Add public key into .ssh/authorized_keys folder on server.
 cat ~/id_rsa.pub >> ~/.ssh/authorized_keys

 Disable ssh login via password.
 sudo vim /etc/ssh/sshd_config

 Set:
 PasswordAuthentication no 
 
 Restart ssh via:
 sudo systemctl restart sshd

## Update Server

 sudo apt-get update
 sudo apt-get upgrade

## Change server name
 sudo nano /etc/hostname

 Look for any old name mentioned in this file:
 sudo nano /etc/hosts

 sudo reboot

## Add user accounts
 sudo useradd -s /path/to/shell -d /home/{dirname} -m -G {secondary-group} {username}
 sudo passwd {username}
 sudo mkdir /home/{username}/.ssh/
 sudo chmod 0700 /home/{username}/.ssh/
 scp {key_pub} user@ip:/home/{username}
 sudo chown -R {username}:{username} /home/{username}/.ssh/

## Mount hdd

## Install docker
 sudo apt-get update
 sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

 Add GLP KEY:
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
 
 Setup directory:
 echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

  Install:
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io

  sudo docker run hello-world

  ### Add user to docker group
  sudo groupadd docker
  sudo usermod -aG docker $USER

  Update group:
  newgrp docker 

  ### Start on Boot

  sudo systemctl enable/disable docker.service
  sudo systemctl enable/disable containerd.service
