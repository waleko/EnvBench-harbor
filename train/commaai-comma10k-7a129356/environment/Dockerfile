FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/commaai/comma10k.git /data/project \
    && cd /data/project \
    && git checkout 7a1293562fd8c0f3932c2c55f6e8a509efa1c66d
