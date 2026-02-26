FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/artesiawater/hydropandas.git /data/project \
    && cd /data/project \
    && git checkout 2426022ead74875a5f5abf6830c405d07533e78c
