These files map to POC use case 4 in https://docs.google.com/document/d/1SK68C_iLNOoVRpgTmdpAp_a7llTemDly-_-Ii11suoE/edit

Build & Run instructions:

0. Download all the files in this directory to local Docker image build directory

1. Replace all instances of "apps.zubat.cf-app.com" (CF Apps Domain name in my env) with yours, in the instructions below and the downloaded files.

2. Download Oracle WLS installer (instructions in Dockerfile)

3. Build the image (instructions in Dockerfile) and push to a repo (I am using DockerHub] so it can be pulled in subsequent steps
- Note this image uses a base java8 image, so build that first, if you haven't done so already
https://github.com/Pivotal-Field-Engineering/weblogic-ee-kubo/tree/master/java8

4. Create persistent storage on IaaS (vSphere in this case) and configure corresponding K8s artifacts around it
- create VMDK file via ESX command line: vmkfstools -c 2G /vmfs/volumes/LUN01/Pods-Disks/Disk1.vmdk
- create Persistent Volume:  kubectl apply -f vsphere-volume-pv.yml --record
- create Persistent Volume Claim:  kubectl apply -f vsphere-volume-pvc.yml --record

5. Deploy image to PKS
- kubectl apply -f wls-jms-statefulset.yml --record
- kubectl label services wls-jms-admin http-route-sync=wls-jms-admin
- kubectl label services wls-jms-console http-route-sync=wls-jms-console

6. WLS Console accessible at http://wls-jms-console.apps.zubat.cf-app.com/console
- username / password is weblogic / welcome1

7. Configure WLS JMS resources
- java weblogic.WLST configure-jms.py
  
8. You can now view/put/get JMS messages on the configured WLS JMS queue (previous step). Given the WLS JMS Filestore is mapped onto persistent IaaS storage (VMDK file in this case), Persistent JMS messages will be able to survive Pod restarts.
