FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/andrew-codechimp/HA-Battery-Notes.git /data/project \
    && cd /data/project \
    && git checkout 59a2b6d544f88deefa1e5a7bcb44a8abf772c62d
