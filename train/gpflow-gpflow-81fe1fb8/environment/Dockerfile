FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/gpflow/gpflow.git /data/project \
    && cd /data/project \
    && git checkout 81fe1fb86a77d3d49d30ab4f8e739e25bbd71f56
