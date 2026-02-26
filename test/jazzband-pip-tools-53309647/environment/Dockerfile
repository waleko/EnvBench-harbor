FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/jazzband/pip-tools.git /data/project \
    && cd /data/project \
    && git checkout 53309647980e2a4981db54c0033f98c61142de0b
