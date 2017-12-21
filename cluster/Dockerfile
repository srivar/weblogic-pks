# Copyright (c) 2014-2017 Oracle and/or its affiliates. All rights reserved.
#
# Licensed under the Universal Permissive License v 1.0 as shown at http://oss.oracle.com/licenses/upl.
#
# REQUIRED FILES TO BUILD THIS IMAGE
# ----------------------------------
# (1) fmw_12.2.1.2.0_wls_supplemental_quick_Disk1_1of1.zip
#     Download the Developer Quick installer from http://www.oracle.com/technetwork/middleware/weblogic/downloads/wls-for-dev-1703574.html
#     Unzip the downloaded file and copy the installer "fmw_12.2.*.*.0_wls_quick.jar" into Docker image build dir
#
# HOW TO BUILD THIS IMAGE
# -----------------------
# Put all downloaded files in the same directory as this Dockerfile
# Run: 
#      $ docker build -t wls-12212-cluster .
#

# Pull base image
# ---------------
FROM localhost:5000/java8:latest

# Maintainer
# ----------
MAINTAINER Rahul Srivastava <rsrivastava@pivotal.io>

# Environment variables required for this build (do NOT change)
# -------------------------------------------------------------
ENV ORACLE_HOME="/u01/oracle/fmw_home" \
    FMW_PKG="fmw_12.2.1.2.0_wls.jar"
ENV MW_HOME="$ORACLE_HOME" \ 
    PATH="$ORACLE_HOME/wlserver/server/bin:$ORACLE_HOME/wlserver/../oracle_common/modules/org.apache.ant_1.9.2/bin:$JAVA_HOME/jre/bin:$JAVA_HOME/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$ORACLE_HOME/oracle_common/common/bin:$ORACLE_HOME/wlserver/common/bin:$ORACLE_HOME/user_projects/domains/medrec/bin:$ORACLE_HOME/wlserver/samples/server/medrec/:$ORACLE_HOME/wlserver/samples/server/:$ORACLE_HOME/wlserver/../oracle_common/modules/org.apache.maven_3.2.5/bin"

ENV TEMPLATE_PATH="$ORACLE_HOME/wlserver/common/templates/wls/wls.jar"
ENV DOMAIN_PATH="/u01/oracle/user_projects/mydomain"


RUN mkdir -p /u01 && \
    chmod a+xr /u01 && \
    useradd -b /u01 -d /u01/oracle -m -s /bin/bash oracle

# Copy supplemental package and scripts
# --------------------------------
COPY $FMW_PKG /u01/oracle
USER root
COPY startSample.sh  /u01/oracle/
COPY create-domain.py /u01/oracle/
COPY oraInst.loc /u01/oracle/
COPY responseFile.txt /u01/oracle/
RUN chmod +xr /u01/oracle/startSample.sh 

# Installation of Weblogic & Coherence
# --------------------------------------------a
USER oracle
RUN cd /u01/oracle && $JAVA_HOME/bin/java -jar /u01/oracle/$FMW_PKG -silent -responseFile `pwd`/responseFile.txt -invPtrLoc /u01/oracle/oraInst.loc && cd - && \
    rm /u01/oracle/$FMW_PKG
RUN set
RUN ls $ORACLE_HOME
RUN $MW_HOME/oracle_common/common/bin/wlst.sh /u01/oracle/create-domain.py

USER root 
RUN chmod +xr /u01/oracle/user_projects/mydomain/*.sh

WORKDIR /u01/oracle/user_projects/mydomain

EXPOSE 7001

CMD ["/u01/oracle/startSample.sh"]
