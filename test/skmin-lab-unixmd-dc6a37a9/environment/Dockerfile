FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/skmin-lab/unixmd.git /data/project \
    && cd /data/project \
    && git checkout dc6a37a9ee4ad6ca72273cf1b697c631d551953c
