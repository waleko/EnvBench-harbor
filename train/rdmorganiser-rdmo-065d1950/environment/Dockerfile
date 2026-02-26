FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/rdmorganiser/rdmo.git /data/project \
    && cd /data/project \
    && git checkout 065d195043b7ac34a7b6b3180dac69829a3974bc
