FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/gazzolalab/miv-os.git /data/project \
    && cd /data/project \
    && git checkout b0005ffe995efffa3f00a26636d563929e187483
