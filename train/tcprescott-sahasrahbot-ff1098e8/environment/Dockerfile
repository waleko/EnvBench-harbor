FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/tcprescott/sahasrahbot.git /data/project \
    && cd /data/project \
    && git checkout ff1098e80c60be704fecfcfa23aa9f28e360384b
