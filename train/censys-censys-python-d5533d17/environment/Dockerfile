FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/censys/censys-python.git /data/project \
    && cd /data/project \
    && git checkout d5533d17175561528757245784b79c41b0578dfc
