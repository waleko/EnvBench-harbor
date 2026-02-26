FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/sublimelinter/sublimelinter.git /data/project \
    && cd /data/project \
    && git checkout 621ba9bf8d4ed4084902b8840bb1ae7d31e6a8fb
