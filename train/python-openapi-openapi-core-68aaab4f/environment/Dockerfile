FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/python-openapi/openapi-core.git /data/project \
    && cd /data/project \
    && git checkout 68aaab4fb8c0d8382ab3d05588b501acaf7a51aa
