FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/emdgroup/baybe.git /data/project \
    && cd /data/project \
    && git checkout 8afb0ff99655d34176fa7dc52ec488e3773103d3
