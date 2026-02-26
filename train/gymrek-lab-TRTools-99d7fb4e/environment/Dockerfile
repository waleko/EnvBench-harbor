FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/gymrek-lab/TRTools.git /data/project \
    && cd /data/project \
    && git checkout 99d7fb4ef0a420e4a689bafecba5189127d657ba
