FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/has2k1/plotnine.git /data/project \
    && cd /data/project \
    && git checkout 812a5ab0b591515c4f5b62c08b5e51f90ab4cae1
