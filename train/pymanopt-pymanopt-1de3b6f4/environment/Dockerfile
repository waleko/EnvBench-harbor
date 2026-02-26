FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pymanopt/pymanopt.git /data/project \
    && cd /data/project \
    && git checkout 1de3b6f47258820fdc072fceaeaa763b9fd263b0
