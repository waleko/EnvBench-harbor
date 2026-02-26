FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/zappa/zappa.git /data/project \
    && cd /data/project \
    && git checkout 39f75e76d28c1a08d4de6501e6f794fe988cbc98
