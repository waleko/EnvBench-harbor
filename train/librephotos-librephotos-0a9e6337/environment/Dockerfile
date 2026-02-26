FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/librephotos/librephotos.git /data/project \
    && cd /data/project \
    && git checkout 0a9e63377333dc4947767fbac81055a07ccf5341
