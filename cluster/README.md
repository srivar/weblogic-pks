These files map to use case 5 in https://docs.google.com/document/d/1SK68C_iLNOoVRpgTmdpAp_a7llTemDly-_-Ii11suoE/edit

Build & Run instructions:

0. Download all the files in this directory to your local Docker image build directory

1. Replace all instances of "apps.zubat.cf-app.com" (CF Apps Domain name in my env) with yours, in the instructions below and the downloaded files.

2. Download Oracle WLS installer (instructions in Dockerfile)

3. Build the Docker image (instructions in Dockerfile) and push to a repo (I am using DockerHub) so it can be pulled in subsequent steps
- Note this image uses a base java8 image, so build that first, if you haven't done so already
https://github.com/Pivotal-Field-Engineering/weblogic-ee-kubo/tree/master/java8

4. Deploy WLS Admin Server to PKS
- kubectl apply -f  wls-adminserver-statefulset.v2.yml --record
- kubectl label services as-console http-route-sync=as-console
- kubectl label services as-admin http-route-sync=as-admin

  WLS Admin Console accessible at http://as-console.apps.zubat.cf-app.com/console
  - username / password is weblogic / welcome1

5. Configure WLS Cluster via the WLST client
- java weblogic.WLST configure-cluster.py

6. Deploy WLS Cluster to PKS
- kubectl apply -f wls-cluster-statefulset.v2.yml --record
- kubectl label services wls-cluster http-route-sync=wls-cluster

7. Deploy test WLS app onto WLS Cluster
- install "tar" on Admin Server pod
  - kubectl exec -ti as-0 /bin/bash
  - yum install tar
- kubectl cp shoppingcart.war as-0:/u01/oracle/user_projects/mydomain/shoppingcart.war
- Deploy the app using the WLS Console

Testapp available at http://wls-cluster.apps.zubat.cf-app.com/shoppingcart/welcome.jsp

8. You can now try deleting K8s Pods ms-0 or ms-1 (sequentially, don't do both at same time!) - the app will continue to function and your shopping cart contents will be preserved, courtesy WLS In-Memory Session Replication across the WLS Cluster members.
