FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/roboflow/supervision.git /data/project \
    && cd /data/project \
    && git checkout d5cebd4fd2b75b160feb9d22b3558f3247b27f28
