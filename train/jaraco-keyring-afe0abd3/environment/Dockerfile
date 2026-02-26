FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/jaraco/keyring.git /data/project \
    && cd /data/project \
    && git checkout afe0abd3165da8fd68d2812f483ba429008442d5
