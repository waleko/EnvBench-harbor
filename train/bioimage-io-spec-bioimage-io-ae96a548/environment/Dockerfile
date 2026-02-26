FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/bioimage-io/spec-bioimage-io.git /data/project \
    && cd /data/project \
    && git checkout ae96a5486e8652ebefd3c23ba1f6d6ca05051a22
