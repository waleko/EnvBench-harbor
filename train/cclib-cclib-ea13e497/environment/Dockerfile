FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/cclib/cclib.git /data/project \
    && cd /data/project \
    && git checkout ea13e497a0ade1d47ecffce9c219f032cfe741d1
