FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/open-pulse/openpulse.git /data/project \
    && cd /data/project \
    && git checkout 1897c63f49c05e762f048bce9f42d120af965240
