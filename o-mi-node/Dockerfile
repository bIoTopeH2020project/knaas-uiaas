FROM openjdk:latest
COPY o-mi-node-0.10.1.tgz .
RUN tar -xzf o-mi-node-0.10.1.tgz && \
    sed -i 's;# Format:;"255.255.255.255/0","ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/0";' o-mi-node-0.10.1/configs/application.conf
EXPOSE 8080
ENTRYPOINT ["o-mi-node-0.10.1/bin/o-mi-node"]
