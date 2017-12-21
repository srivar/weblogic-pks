connect('weblogic','welcome1','http://wls-jms-admin.apps.zubat.cf-app.com:80')
edit()
startEdit()

cd('/')
cmo.createFileStore('FileStore-AS')

cd('/FileStores/FileStore-AS')
cmo.setDirectory('/data/filestores')
set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

cd('/')
cmo.createJMSServer('JMSServer-AS')

cd('/JMSServers/JMSServer-AS')
cmo.setPersistentStore(getMBean('/FileStores/FileStore-AS'))
set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

cd('/')
cmo.createJMSSystemResource('SystemModule-0')

cd('/JMSSystemResources/SystemModule-0')
set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

cmo.createSubDeployment('JMSModule-0')

cd('/JMSSystemResources/SystemModule-0/SubDeployments/JMSModule-0')
set('Targets',jarray.array([ObjectName('com.bea:Name=JMSServer-AS,Type=JMSServer')], ObjectName))

set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server'), ObjectName('com.bea:Name=JMSServer-AS,Type=JMSServer')], ObjectName))

set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server'), ObjectName('com.bea:Name=JMSServer-AS,Type=JMSServer')], ObjectName))

cd('/JMSSystemResources/SystemModule-0/JMSResource/SystemModule-0')
cmo.createQueue('Queue-0')

cd('/JMSSystemResources/SystemModule-0/JMSResource/SystemModule-0/Queues/Queue-0')
cmo.setJNDIName('Queue-0-JNDI')
cmo.setSubDeploymentName('JMSModule-0')

cd('/JMSSystemResources/SystemModule-0/SubDeployments/JMSModule-0')
set('Targets',jarray.array([ObjectName('com.bea:Name=JMSServer-AS,Type=JMSServer')], ObjectName))

activate()

