#!/bin/bash

DB_NAME="be_180320"
DB_USER="be_180320"
DB_PASSWORD="root"
DB_ROOT_PASSWORD="student"
SHOP_URL="localhost:18032"
SHOP_SSL_URL="localhost:18033"

mysql -p$DB_ROOT_PASSWORD -e "DROP DATABASE IF EXISTS ${DB_NAME};"
mysql -p$DB_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS ${DB_NAME};"
mysql -p$DB_ROOT_PASSWORD -e "USE ${DB_NAME};"
mysql -p$DB_ROOT_PASSWORD -e "CREATE USER IF NOT EXISTS ${DB_USER}@'%' IDENTIFIED BY '${DB_PASSWORD}';"
mysql -p$DB_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'%';"
mysql -p$DB_ROOT_PASSWORD -e "FLUSH PRIVILEGES;"
mysql -u $DB_USER -p$DB_PASSWORD $DB_NAME < /tmp/${DB_NAME}.sql

mysql -u $DB_USER -p$DB_PASSWORD $DB_NAME -e "UPDATE ps_shop_url SET domain='${SHOP_URL}', domain_ssl='${SHOP_SSL_URL}' WHERE id_shop_url=1;" 