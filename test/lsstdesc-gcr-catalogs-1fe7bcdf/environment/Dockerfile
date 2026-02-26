FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/lsstdesc/gcr-catalogs.git /data/project \
    && cd /data/project \
    && git checkout 1fe7bcdfe464c7094b593f0a460df7d534363ce7
