FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mirageoscience/geoapps.git /data/project \
    && cd /data/project \
    && git checkout 9dd62db0137dfe554fc550b57c58b0be521a1749
