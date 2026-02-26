FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/timbrel/gitsavvy.git /data/project \
    && cd /data/project \
    && git checkout da8f3ca24b2cdac43fe4d6f1d7a2c47d02d04b2a
