FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/jackdewinter/pymarkdown.git /data/project \
    && cd /data/project \
    && git checkout 446fbbf251f5daa150b967b90c72216aeddb73fc
