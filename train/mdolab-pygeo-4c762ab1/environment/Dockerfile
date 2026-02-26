FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mdolab/pygeo.git /data/project \
    && cd /data/project \
    && git checkout 4c762ab13e4b8847e346e4c269f7d63c375bec74
