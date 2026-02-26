FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/automl/neps.git /data/project \
    && cd /data/project \
    && git checkout 6a6c0c273f59036b8605086c43a6a714ea02bd23
