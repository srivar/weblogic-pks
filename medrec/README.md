This corresponds to use case 2 in https://docs.google.com/document/d/1SK68C_iLNOoVRpgTmdpAp_a7llTemDly-_-Ii11suoE/edit#

"MedRec" (Medical Records application) is the reference out-of-box JEE sample app shipped with WLS https://docs.oracle.com/cd/E13222_01/wls/docs81/medrec_tutorials/overview.html

Build and Test instructions:

1. Clone Oracle docker repo https://github.com/oracle/docker-images/tree/master/OracleWebLogic

2. Build base Java 8 image https://github.com/Pivotal-Field-Engineering/weblogic-ee-kubo/tree/master/java8

3. Build base WLS 12.2.1.2 developer image
    - [first build base Java 8 image - previous]
    - cd  OracleWebLogic/dockerfiles
    - sh buildDockerImage.sh -v 12.2.1.2 -d -s

4. Build MedRec image
    - [first build base WLS 12.2.1.2 developer image - previous]
    - cd OracleWebLogic/samples/12212-medrec
    - docker build -t wls-12212-medrec .
    - Push the image to a repo (I am using DockerHub) so it can be pulled in subsequent steps
    
5. Deploy image to PKS
    - kubectl apply -f wls-medrec-deployment.yml --record
    - kubectl apply -f wls-medrec-service.v2.yml --record
    - kubectl label services wls-medrec http-route-sync=wls-medrec

MedRec app available at http://wls-medrec.apps.zubat.cf-app.com/medrec/
(replace "apps.zubat.cf-app.com" with your CF Apps Domain name)

WLS Console available at http://wls-medrec.apps.zubat.cf-app.com/console/
(replace "apps.zubat.cf-app.com" with your CF Apps Domain name)
    - username / password is weblogic / welcome1
