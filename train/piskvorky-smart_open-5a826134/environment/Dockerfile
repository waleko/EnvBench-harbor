FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/piskvorky/smart_open.git /data/project \
    && cd /data/project \
    && git checkout 5a826134eb23c86087d06db3b78b25484e7e2e6d
