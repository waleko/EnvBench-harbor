FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/apiflask/apiflask.git /data/project \
    && cd /data/project \
    && git checkout d71d64a3e4b18ce74129de103e364a321ee33b66
