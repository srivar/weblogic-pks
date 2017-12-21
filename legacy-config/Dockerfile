
# Pull base image
# ---------------
FROM localhost:5000/java8:latest

# Maintainer
# ----------
MAINTAINER Rahul Srivastava <rsrivastava@pivotal.io>

RUN mkdir -p /u01 && \
    chmod a+xr /u01 && \
    useradd -b /u01 -d /u01/oracle -m -s /bin/bash oracle

USER root
COPY startSample.sh  /u01/oracle/
RUN chmod +xr /u01/oracle/startSample.sh 

WORKDIR /u01/oracle

USER oracle

CMD ["/u01/oracle/startSample.sh"]
