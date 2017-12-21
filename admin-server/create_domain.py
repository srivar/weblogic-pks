#!/usr/bin/python
import os, sys
set('DebugEnabled', 'true')

# set to path to template. ex: /u01/oracle/fmw_home/wlserver/common/templates/wls/wls.jar
templatePath=os.getenv('TEMPLATE_PATH')

# ex: /u01/oracle/fmw_home/user_projects/domains/basedomain
domainPath=os.getenv('DOMAIN_HOME')
readTemplate(templatePath, 'Expanded')

cd('/')
cd('Security/base_domain/User/weblogic')
set('Name','weblogic')
cmo.setPassword('p1v0tal!')
cd('/Server/AdminServer')
cmo.setName('AdminServer')
cmo.setListenPort(7011)
cmo.setListenAddress('0.0.0.0')
print('Finalizing the changes')
writeDomain(domainPath)
updateDomain()
closeDomain()
exit()

