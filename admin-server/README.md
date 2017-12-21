This Dockerfile builds a fresh container image from Oracle's FMW installer.   It uses the silent install process for laying down the bits inside the container, then creates a basics WLS Domain definition using WLST.

Basic steps to use this Dockerfile

1. Using a private Docker registry, build and tag a base Oracle Java image using this repo: https://github.com/oracle/docker-images/tree/master/OracleJava/java-8

2. Download the generic Oracle FMW installer from http://www.oracle.com/technetwork/middleware/weblogic/downloads/wls-main-097127.html

3. Unzip and move Jar file to this directory (e.g. fmw_12.2.1.2.0_wls.jar)

4. Touch up create_domain.py per your WLS requirements

5. docker build .

6. docker tag <resulting image> <private registry>/wls-ee-admin:latest
  
7. docker push <private registry>/wls-ee-admin:latest
  
  8. Test in local docker with:  docker run -d -p 7011:7011 -m 4GB -e USER_MEM_ARGS="-Xms2G -Xmx2G" localhost:5000/wls-ee-admin:latest

9. 
