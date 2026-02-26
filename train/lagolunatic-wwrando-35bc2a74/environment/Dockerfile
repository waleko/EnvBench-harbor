FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/lagolunatic/wwrando.git /data/project \
    && cd /data/project \
    && git checkout 35bc2a746713c1a380b6486809a3d87c5ba9fa85
