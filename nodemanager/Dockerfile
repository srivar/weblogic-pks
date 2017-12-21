FROM registry.cf.wrightcode.net:4000/wls-ee-admin:latest

# Maintainer
# ----------
MAINTAINER Monica Riccelli <monica.riccelli@oracle.com>

# Environment variables required for this build (do NOT change)
# -------------------------------------------------------------
ENV ORACLE_HOME="/u01/oracle/fmw_home" 
ENV MW_HOME="$ORACLE_HOME" \ 
    PATH="/u01/oracle:$ORACLE_HOME/wlserver/server/bin:$ORACLE_HOME/wlserver/../oracle_common/modules/org.apache.ant_1.9.2/bin:$JAVA_HOME/jre/bin:$JAVA_HOME/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$ORACLE_HOME/oracle_common/common/bin:$ORACLE_HOME/wlserver/common/bin:$ORACLE_HOME/user_projects/domains/medrec/bin:$ORACLE_HOME/wlserver/samples/server/medrec/:$ORACLE_HOME/wlserver/samples/server/:$ORACLE_HOME/wlserver/../oracle_common/modules/org.apache.maven_3.2.5/bin"

ENV TEMPLATE_PATH="$ORACLE_HOME/wlserver/common/templates/wls/wls.jar"
ENV DOMAIN_HOME="/u01/oracle/user_projects/mydomain"


USER root
COPY startNM.sh  /u01/oracle/
COPY register_machine.py /u01/oracle/
COPY oraInst.loc /u01/oracle/

RUN mkdir $ORACLE_HOME/oracle_common/common/nodemanager

COPY nodemanager.properties $ORACLE_HOME/oracle_common/common/nodemanager/

RUN chmod +xr /u01/oracle/startNM.sh 

# Installation of Weblogic & Coherence
# --------------------------------------------a

WORKDIR /u01/oracle/user_projects/mydomain

EXPOSE 7011 5556

CMD ["startNM.sh"]
