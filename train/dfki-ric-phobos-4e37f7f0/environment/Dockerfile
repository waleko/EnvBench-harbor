FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/dfki-ric/phobos.git /data/project \
    && cd /data/project \
    && git checkout 4e37f7f0f73b1d2a32cb715dd803dcd117f14d21
