#!/bin/sh
# scritp should be run with env variables. i.e: sudo -E ./setup_db.sh

#echo "Setting up the postgreSQL database for Django"
#dbname=${EUPRIME_TOOLKIT_DB_NAME?"Need to set environment variables"}
#dbuser=${EUPRIME_TOOLKIT_DB_USERNAME?"Need to set environment variables"}
#dbpass=${EUPRIME_TOOLKIT_DB_PASSWORD?"Need to set environment variables"}

#su - postgres <<EOF
#psql -U postgres -c "CREATE USER \"$dbuser\" WITH PASSWORD '$dbpass';"
#psql -U postgres -c "CREATE DATABASE \"$dbname\" WITH OWNER \"$dbuser\";"
#psql -U postgres -c "ALTER USER \"$dbuser\" CREATEDB;"
#EOF

echo "Setting up the MySQL database for Django"
dbname=${EUPRIME_TOOLKIT_DB_NAME? "Need to set environment variables"}

echo "Enter the MySQL root password to set up the Database"
mysql -u root -p <<EOF
CREATE DATABASE $dbname;
GRANT ALL PRIVILEGES ON *.* TO root;
EOF

