FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/openreview/openreview-py.git /data/project \
    && cd /data/project \
    && git checkout 799d93b4c49b29e4da805810ba27f1cfa75beeba
