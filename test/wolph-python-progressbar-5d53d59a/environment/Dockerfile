FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/wolph/python-progressbar.git /data/project \
    && cd /data/project \
    && git checkout 5d53d59a37247dd9e4663dd86ca79b16cbc92d9b
