FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/qiboteam/qibocal.git /data/project \
    && cd /data/project \
    && git checkout 0625d904216ddbcfe5a12b46b31e84f04de9285e
