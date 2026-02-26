FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/miurahr/aqtinstall.git /data/project \
    && cd /data/project \
    && git checkout ac7da38299fc56ae4818ff1c19b96e4e2d6f36c8
