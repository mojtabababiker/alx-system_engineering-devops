#!/usr/bin/env bash
# an automated script to install the certbot software
# and create a ssl certificate
# this code requier snap preinstalled

# remove any preinstallde certbot
apt-get remove certbot

# install the certbot
snap install --classic certbot

# create a link for the certbot on the usr/bin/certbot directory
ln -s /snap/bin/certbot /usr/bin/certbot

# stop the haproxy process to create the ssl cert
service haproxy stop

# create the ssl cert
certbot certonly --standalone > cert_files_path

