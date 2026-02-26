FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/roshan-research/hazm.git /data/project \
    && cd /data/project \
    && git checkout d97a5ba13a680a29f2ae5bc6f862e941329890fb
