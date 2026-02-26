FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/astropy/regions.git /data/project \
    && cd /data/project \
    && git checkout 15393a984d1bd93333805b4f0a9277e3e1ed7929
