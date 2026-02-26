FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/nextcord/nextcord.git /data/project \
    && cd /data/project \
    && git checkout 3c4522b0059b756c8cffdbfd956bf4864b013a6c
