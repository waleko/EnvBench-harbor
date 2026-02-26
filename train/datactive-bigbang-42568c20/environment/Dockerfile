FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/datactive/bigbang.git /data/project \
    && cd /data/project \
    && git checkout 42568c20e318bd351a1d42acda21895960646133
