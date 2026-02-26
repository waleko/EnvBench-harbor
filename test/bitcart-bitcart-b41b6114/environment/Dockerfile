FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/bitcart/bitcart.git /data/project \
    && cd /data/project \
    && git checkout b41b61147c32c7baa6376c1f6c5f0fe9357a332d
