#!/bin/sh

USERNAME=${USERNAME:-weblogic}
PASSWORD=${PASSWORD:-welcome1}
ADMIN_SERVER_URL=${ADMIN_SERVER_URL:-NONE}

# WLS deployed as K8s StatefulSet
# Managed Servers will be named as "<K8s_STATEFULSET_NAME>-0", "<K8s_STATEFULSET_NAME>-1", etc.
# "uname --nodename" reflects that name
PODNAME=$(uname --nodename)

# if Admin Server URL is specified (as env variable in K8s YML file), this is a Managed Server
echo "...ADMIN_SERVER_URL = $ADMIN_SERVER_URL, PODNAME = $PODNAME..."
if [ "$ADMIN_SERVER_URL" == "NONE" ]
then
    /u01/oracle/user_projects/mydomain/startWebLogic.sh -Dweblogic.management.username=$USERNAME -Dweblogic.management.password=$PASSWORD
else
    cd /u01/oracle/user_projects/mydomain/bin
    sh ./startManagedWebLogic.sh $PODNAME $ADMIN_SERVER_URL -Dweblogic.management.username=$USERNAME -Dweblogic.management.password=$PASSWORD
fi
