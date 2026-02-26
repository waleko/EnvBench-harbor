FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/bradenm/micropy-cli.git /data/project \
    && cd /data/project \
    && git checkout ac85e9f12c4d71a46f589d716e37c8da33f761a7
