FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/postgrespro/mamonsu.git /data/project \
    && cd /data/project \
    && git checkout 31a59811d7f66f01c90d77b9df34f3077a12dd8b
