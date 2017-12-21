#!/usr/bin/python
#
# Copyright (c) 2014-2017 Oracle and/or its affiliates. All rights reserved.
#
# Licensed under the Universal Permissive License v 1.0 as shown at http://oss.oracle.com/licenses/upl.
#
import os, sys
set('DebugEnabled', 'true')

# set to path to template. ex: /u01/oracle/fmw_home/wlserver/common/templates/wls/wls.jar
templatePath=os.getenv('TEMPLATE_PATH')

# ex: /u01/oracle/fmw_home/user_projects/domains/basedomain
domainPath=os.getenv('DOMAIN_PATH')
readTemplate(templatePath, 'Expanded')

cd('/')
cd('Security/base_domain/User/weblogic')
set('Name','weblogic')
cmo.setPassword('welcome1')
cd('/Server/AdminServer')
cmo.setName('AdminServer')
cmo.setListenPort(7001)

# WLS deployed as K8s StatefulSet, Pod will have a stable DNS name "<STATEFULSETNAME>-0.<STATEFULSETNAME>.."
cmo.setListenAddress('wls-jms-0.wls-jms.default.svc.cluster.local')

# enable Tunneling and configure Network Channel for T3/HTTP tunneling over CF HTTP Proxy
# for WLST client
cmo.setTunnelingEnabled(true)

create('Channel-0','NetworkAccessPoint')
cd('NetworkAccessPoints/Channel-0')
cmo.setProtocol('http')
# ListenAddress set to stable DNS of Pod
cmo.setListenAddress('wls-jms-0.wls-jms.default.svc.cluster.local')
cmo.setListenPort(7011)
# PublicAddress set to CF HAProxy front-end to K8s cluster
cmo.setPublicAddress('wls-jms-admin.apps.zubat.cf-app.com')
cmo.setPublicPort(80)
cmo.setEnabled(true)
cmo.setHttpEnabledForThisProtocol(true)
cmo.setTunnelingEnabled(true)
cmo.setOutboundEnabled(true)
cmo.setTwoWaySSLEnabled(false)
cmo.setClientCertificateEnforced(false)


print('Finalizing the changes')
writeDomain(domainPath)
updateDomain()
closeDomain()
exit()
