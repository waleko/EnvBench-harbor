FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/eylles/pywal16.git /data/project \
    && cd /data/project \
    && git checkout ab1f5c87f1a8b8423d66cab3cb7d0b4df9f47636
