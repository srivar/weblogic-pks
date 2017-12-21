#!/usr/bin/python
import os, sys
set('DebugEnabled', 'true')

# set to path to template. ex: /u01/oracle/fmw_home/wlserver/common/templates/wls/wls.jar
templatePath=os.getenv('TEMPLATE_PATH')

# ex: /u01/oracle/fmw_home/user_projects/domains/basedomain
domainPath=os.getenv('DOMAIN_HOME')
readTemplate(templatePath, 'Expanded')

wlUsername=os.getenv('USERNAME')
wlPassword=os.getenv('PASSWORD')
wlAdminUrl="t3://"+os.getenv('WL_HOST')+":"+os.getenv('WL_PORT')

connect(wlUsername,wlPassword,wlAdminUrl)

nmEnroll(domainPath, domainPath+"/nodemanager")
print('Finalizing the changes')
exit()

