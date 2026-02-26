FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ethereum/py-evm.git /data/project \
    && cd /data/project \
    && git checkout d8df507e42c885ddeca2b64bbb8f10705f075d3e
