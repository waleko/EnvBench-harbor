FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/menpo/menpo.git /data/project \
    && cd /data/project \
    && git checkout bf08b913bb84ba5f5323e9b7d372a8349b9d1fa8
