FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/numba/llvmlite.git /data/project \
    && cd /data/project \
    && git checkout 5c181ff3af1de04d4bd70fb0ee287aa81d1fe198
