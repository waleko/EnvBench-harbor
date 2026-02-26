FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/vacanza/python-holidays.git /data/project \
    && cd /data/project \
    && git checkout 472e89d889cf3a5c5301d54bc642f6c149f55ee5
