#!/bin/sh

# WLS deployed as K8s StatefulSet
# WLS instances will be named as "<K8s_STATEFULSET_NAME>-0", "<K8s_STATEFULSET_NAME>-1", etc.
# "uname --nodename" reflects that name
PODNAME=$(uname --nodename)
echo "...PODNAME = $PODNAME..."

USERNAME=${USERNAME:-weblogic}
PASSWORD=${PASSWORD:-welcome1}
/u01/oracle/user_projects/mydomain/startWebLogic.sh -Dweblogic.management.username=$USERNAME -Dweblogic.management.password=$PASSWORD
