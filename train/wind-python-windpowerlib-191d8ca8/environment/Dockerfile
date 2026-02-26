FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/wind-python/windpowerlib.git /data/project \
    && cd /data/project \
    && git checkout 191d8ca894d6d830997630fa3599f048d6e8c7b4
