FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/cda-tum/mqt-bench.git /data/project \
    && cd /data/project \
    && git checkout ae62809395e5b31b5f5b5886f3e5916193029cdd
