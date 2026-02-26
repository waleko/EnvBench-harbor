FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/r-anime/holo.git /data/project \
    && cd /data/project \
    && git checkout 7864bc6d8359f0eead242e015398fdb1aaebd3cb
