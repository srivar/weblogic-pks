These files map to POC use case 6 in https://docs.google.com/document/d/1SK68C_iLNOoVRpgTmdpAp_a7llTemDly-_-Ii11suoE/edit#

This directory captures the second part of the test where we create a container that accesses and boots up a previously-created WLS Domain on persistent storage that's mapped to the container.

The first part of the test is under https://github.com/Pivotal-Field-Engineering/weblogic-ee-kubo/tree/master/unix-server. Complete that first part before you do the below.

Build & Run instructions:

0. Build a base java8 image if you haven't done so already
https://github.com/Pivotal-Field-Engineering/weblogic-ee-kubo/tree/master/java8

1. Download all the files in this directory to local Docker image build directory

2. Build a docker image and push to a repo (I am using DockerHub)
	- docker build -t srivar/wls-12-legacy .
	- docker push srivar/wls-12-legacy

3. Create a K8s Deployment: kubectl apply -f wls-legacy-deployment.yml --record
	- note the K8s Volume (prevously created in part 1 of this test) is mounted as "/data/wls-home"
	- note we are specifying an environment variable "DOMAIN_HOME" that points to the location of the WLS Domain (previously created in part 1 of this test)
	- if you've specified WLS username/passwords different from the default ("weblogic"/"welcome1"), you need to specify those via additional environment variables "USERNAME" and "PASSWORD"

4. The "startSample.sh" script (called from within the Dockerfile) will automatically start the previously configured WLS Domain

5. Create a K8s Service and setup CF Routing
	- kubectl apply -f wls-legacy-service.yml --record
	- kubectl label services wls-legacy http-route-sync=wls-legacy
	
6. The WLS Admin Console is now accessible at http://wls-legacy.apps.zubat.cf-app.com/console
	- replace "apps.zubat.cf-app.com" with your CF App Domain name
	
