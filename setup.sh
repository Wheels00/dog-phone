#!/bin/bash

echo "Setting up Dog Phone"

echo "Installing dependencies"

apt-get -y install python3-pip
pip3 install Flask
pip3 install -U Flask-WTF
pip3 install Flask-Bootstrap
pip3 install pyserial

echo "Setting up services to run on boot"

sudo cp webapp/dog-phone-webapp.service /lib/systemd/system/dog-phone-webapp.service
sudo chmod 644 /lib/systemd/system/dog-phone-webapp.service
sudo systemctl daemon-reload
sudo systemctl enable dog-phone-webapp.service

# TODO add setup of dog-phone-main service 


echo "Make wpa_supplicant.conf writeable"

sudo chmod 604 /etc/wpa_supplicant/wpa_supplicant.conf