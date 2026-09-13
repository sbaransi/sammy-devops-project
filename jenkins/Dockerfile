FROM jenkins/jenkins:lts

USER root

COPY certs/ZscalerRootCA.crt /usr/local/share/ca-certificates/ZscalerRootCA.crt

RUN update-ca-certificates && \
    keytool -importcert \
    -trustcacerts \
    -noprompt \
    -alias zscaler-root-ca \
    -file /usr/local/share/ca-certificates/ZscalerRootCA.crt \
    -keystore $JAVA_HOME/lib/security/cacerts \
    -storepass changeit

USER jenkins
