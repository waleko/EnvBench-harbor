FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mpmath/mpmath.git /data/project \
    && cd /data/project \
    && git checkout ee1a8102665a2fba0faba6c2c0f0a064de92b522
