FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/sphinx-contrib/spelling.git /data/project \
    && cd /data/project \
    && git checkout 51debaa98520145f6debce8f5a6c6d220359f54c
