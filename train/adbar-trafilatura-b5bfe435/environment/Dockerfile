FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/adbar/trafilatura.git /data/project \
    && cd /data/project \
    && git checkout b5bfe43520623a5e42c6e4034878ec8dd7d9d242
