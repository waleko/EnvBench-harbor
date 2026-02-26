FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/learning-and-intelligent-systems/predicators.git /data/project \
    && cd /data/project \
    && git checkout 00c42d6817f661604165a6f7d97dceb4ed3d55a9
