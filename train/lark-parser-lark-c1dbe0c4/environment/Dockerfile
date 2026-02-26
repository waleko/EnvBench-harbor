FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/lark-parser/lark.git /data/project \
    && cd /data/project \
    && git checkout c1dbe0c49701cd37c595492d1461a97c0597215c
