connect('weblogic','welcome1','http://as-admin.apps.zubat.cf-app.com:80')
edit()
startEdit()

cd('/')
cmo.createServer('ms-0')

cd('/Servers/ms-0')
cmo.setListenAddress('ms-0.ms.default.svc.cluster.local')
cmo.setListenPort(7001)
#cmo.setPreferredSecondaryGroup('replicationGroup2')
#cmo.setReplicationGroup('replicationGroup1')

cd('/')
cmo.createCluster('cluster-0')

cd('/Clusters/cluster-0')
cmo.setClusterMessagingMode('unicast')
cmo.setClusterBroadcastChannel('')
#cmo.setPreferredSecondaryGroup('replicationGroup2')
#cmo.setReplicationGroup('replicationGroup1')

cd('/Servers/ms-0')
cmo.setCluster(getMBean('/Clusters/cluster-0'))

activate()

startEdit()

cd('/')
cmo.createServer('ms-1')

cd('/Servers/ms-1')
cmo.setListenAddress('ms-1.ms.default.svc.cluster.local')
cmo.setListenPort(7001)
cmo.setCluster(getMBean('/Clusters/cluster-0'))

activate()
