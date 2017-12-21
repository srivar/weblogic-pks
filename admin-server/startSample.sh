#!/bin/sh
#
# Copyright (c) 2015 Oracle and/or its affiliates. All rights reserved.
#

# Define default command to create medrec domain 
USERNAME=${USERNAME:-weblogic}
PASSWORD=${PASSWORD:-p1v0tal!}

${DOMAIN_HOME}/startWebLogic.sh -Dweblogic.management.username=$USERNAME -Dweblogic.management.password=$PASSWORD
