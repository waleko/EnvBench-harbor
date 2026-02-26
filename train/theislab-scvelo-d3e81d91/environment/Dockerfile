FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/theislab/scvelo.git /data/project \
    && cd /data/project \
    && git checkout d3e81d91e8c31c42d1a4b3baae8b4fe2e9671d45
