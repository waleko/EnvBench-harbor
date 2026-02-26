FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/columnflow/columnflow.git /data/project \
    && cd /data/project \
    && git checkout ad04770a757f5031229ea1b47314cef6de5c9edf
