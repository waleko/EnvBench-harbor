FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pokepetter/ursina.git /data/project \
    && cd /data/project \
    && git checkout 22b580f50944d8a940e0a6e16f3e75f1601703a3
