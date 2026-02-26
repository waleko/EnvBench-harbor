FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mollie/mollie-api-python.git /data/project \
    && cd /data/project \
    && git checkout 957b44fddb9d4d833508120022c7f291f5ca8d06
