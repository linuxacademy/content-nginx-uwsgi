#!/bin/bash

read -p "Host: " host
read -p "Database Name: " db_name
read -p "Database User: " db_user
read -s -p "Database Password: " db_password

sed -e "s/\${db_name}/${db_name}/" \
	-e "s/\${db_user}/${db_user}/" \
	-e "s/\${db_password}/${db_password}/" \
	-e "s#\${project_dir}#${PWD}#" \
	-e "s#\${host}#${host}#" \
	systemd/notes.uwsgi.template > /etc/systemd/system/notes.uwsgi.service

mkdir -p /var/www/${host}
chown -R nginx:nginx /var/www/${host}

echo " "
