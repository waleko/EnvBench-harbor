FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/nschloe/meshio.git /data/project \
    && cd /data/project \
    && git checkout b2ee99842e119901349fdeee06b5bf61e01f450a
