FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/cantools/cantools.git /data/project \
    && cd /data/project \
    && git checkout 2c92c60f2d1b50894ad0c5652afd331283e03402
