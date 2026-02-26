FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pypose/pypose.git /data/project \
    && cd /data/project \
    && git checkout 931dc6f496936792059806eee190b9d6755c8c6f
