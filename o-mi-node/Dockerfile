FROM openjdk:latest
COPY o-mi-node-1.0.9.tgz .
RUN tar -xzf o-mi-node-1.0.9.tgz && \
    sed -i 's;# Format:;"255.255.255.255/0","ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/0";' o-mi-node-1.0.9/conf/application.conf
EXPOSE 8080
ENTRYPOINT ["o-mi-node-1.0.9/bin/o-mi-node"]
