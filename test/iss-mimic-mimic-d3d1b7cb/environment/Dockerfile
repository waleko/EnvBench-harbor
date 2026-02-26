FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/iss-mimic/mimic.git /data/project \
    && cd /data/project \
    && git checkout d3d1b7cbbca38dd039ae47223517587758c1a9d5
