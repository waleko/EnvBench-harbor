FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/qiboteam/qibo.git /data/project \
    && cd /data/project \
    && git checkout 1bb08d9dab45205875073c371ea4fcefa982221f
