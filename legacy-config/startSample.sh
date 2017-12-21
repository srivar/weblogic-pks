#!/bin/sh

USERNAME=${USERNAME:-weblogic}
PASSWORD=${PASSWORD:-welcome1}
DOMAIN_HOME=${DOMAIN_HOME:-NONE}

# if domain directory is specified (as env variable in K8s YML file), go into that directory and start
# the Admin Server. Else write our error message and exit out.
echo "...DOMAIN_HOME = $DOMAIN_HOME..."
if [ "$DOMAIN_HOME" == "NONE" ]
then
    echo "Error! No WLS Domain home directory specified.. exiting.."
else
    cd $DOMAIN_HOME
    sh ./startWebLogic.sh -Dweblogic.management.username=$USERNAME -Dweblogic.management.password=$PASSWORD
fi
