FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/islandora/documentation.git /data/project \
    && cd /data/project \
    && git checkout d9b18ffb2678dfcf2f5d20cd36de0de2aacef528
