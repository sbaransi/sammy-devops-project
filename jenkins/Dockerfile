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

# Install Docker CLI
RUN apt-get update && \
    apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

USER jenkins
