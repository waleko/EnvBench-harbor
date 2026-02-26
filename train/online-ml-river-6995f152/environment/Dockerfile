FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/online-ml/river.git /data/project \
    && cd /data/project \
    && git checkout 6995f1522a9136fd3982890afac5c4a178e4cd57
