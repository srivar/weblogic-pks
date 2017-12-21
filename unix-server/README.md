
These files map to POC use case 6 in https://docs.google.com/document/d/1SK68C_iLNOoVRpgTmdpAp_a7llTemDly-_-Ii11suoE/edit#

This directory captures the first part of the test where we create an empty Linux container, install WLS and create a WLS Domain on persistent storage that's mapped to the container.

The second part of the test is under https://github.com/Pivotal-Field-Engineering/weblogic-ee-kubo/tree/master/legacy-config. Proceed there after you've completed the below.

Build & Run instructions:

0. Build a base java8 image if you haven't done so already
https://github.com/Pivotal-Field-Engineering/weblogic-ee-kubo/tree/master/java8

1. Download all the files in this directory to local Docker image build directory

2. Build a docker image and push to a repo (I am using DockerHub)
	- docker build -t srivar/unix-server .
	- docker push srivar/unix-server

3. Create persistent storage on IaaS (vSphere in this case) and configure corresponding K8s artifacts around it
	- create VMDK file via ESX command line: vmkfstools -c 3G /vmfs/volumes/LUN01/Pods-Disks/Disk2.vmdk
	- create Persistent Volume: kubectl apply -f vsphere-volume-pv2.yml --record
	- create Persistent Volume Claim: kubectl apply -f vsphere-volume-pvc2.yml --record

4. Create a K8s Deployment for your empty Linux container: kubectl apply -f unix-server-deployment.yml --record
	- note the previously created K8s Volume is mounted as "/data/wls-home"
	- note we are specifying a startup command of "sleep infinity" to keep this container up and running
	- install "tar" on the container
		- kubectl exec -ti <CONTAINER_NAME> /bin/bash
		- yum install tar
	
5. On your laptop, download the Oracle WLS installer
	- Accept license agreement and download "Oracle Weblogic Server 12cR2 (12.2...) Quick Installer for Developers" from http://www.oracle.com/technetwork/middleware/fusion-middleware/downloads/index.html
	- Unzip downloaded file and copy the JAR to your container
		- kubectl cp fmw_12.2.1.3.0_wls_quick.jar <CONTAINER_NAME>:/data/wls-home/fmw_12.2.1.3.0_wls_quick.jar

6. Install WLS on your container and create a new WLS Domain
	- kubectl exec -ti <CONTAINER_NAME> /bin/bash
	- cd /data/wls-home
	- java -jar fmw_12.2.1.3.0_wls_quick.jar
	- . wlserver/server/bin/setWLSEnv.sh
	- cd /data/wls-home
	- java weblogic.Server
		- remember the "username" and "password" you specify here, you'll need them later
	- note the previous command ("java weblogic.Server") is a nice feature in WLS - it generates a new WLS Domain if one is not found in the current working directory. Easiest way to create a new WLS Domain.

7. Delete the K8s Deployment (you created in step #4 above).

The WLS install and Domain you created above are on a NAS that'll subsequently be accessed from another container.

Proceed to second part of this test - https://github.com/Pivotal-Field-Engineering/weblogic-ee-kubo/tree/master/legacy-config


