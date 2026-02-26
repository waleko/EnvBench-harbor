FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/qiboteam/qibolab.git /data/project \
    && cd /data/project \
    && git checkout 5e8ed94a7336734a9babca39ba58f1c557865d0e
