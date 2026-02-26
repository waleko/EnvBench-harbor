FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/Mirascope/mirascope.git /data/project \
    && cd /data/project \
    && git checkout cd6bf0a92d2dae975081d6da8281097abb5810a1
