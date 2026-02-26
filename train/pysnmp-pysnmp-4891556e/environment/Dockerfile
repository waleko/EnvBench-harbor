FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pysnmp/pysnmp.git /data/project \
    && cd /data/project \
    && git checkout 4891556e7db831a5a9b27d4bad8ff102609b2a2c
