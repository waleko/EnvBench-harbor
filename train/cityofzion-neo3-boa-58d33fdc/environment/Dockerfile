FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/cityofzion/neo3-boa.git /data/project \
    && cd /data/project \
    && git checkout 58d33fdcbb67cc6d4f5efefced4ef0a382346ad4
