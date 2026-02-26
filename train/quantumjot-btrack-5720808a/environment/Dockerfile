FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/quantumjot/btrack.git /data/project \
    && cd /data/project \
    && git checkout 5720808a3533a91b02cb521c787b8ac31d3df20d
