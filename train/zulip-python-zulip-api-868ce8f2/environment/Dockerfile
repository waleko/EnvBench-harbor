FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/zulip/python-zulip-api.git /data/project \
    && cd /data/project \
    && git checkout 868ce8f225b82f628c48284ac91feb4c2c6a48cc
