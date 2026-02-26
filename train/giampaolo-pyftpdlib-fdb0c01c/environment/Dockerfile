FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/giampaolo/pyftpdlib.git /data/project \
    && cd /data/project \
    && git checkout fdb0c01ca29e43b860d3d0b743a09833abc18c3c
