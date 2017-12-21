#!/bin/sh
#
# Copyright (c) 2015 Oracle and/or its affiliates. All rights reserved.
#

# Define default command to create medrec domain 
USERNAME=${USERNAME:-weblogic}
PASSWORD=${PASSWORD:-p1v0tal!}
${ORACLE_HOME}/oracle_common/common/bin/wlst.sh /u01/oracle/register_machine.py
${ORACLE_HOME}/wlserver/server/bin/startNodeManager.sh
