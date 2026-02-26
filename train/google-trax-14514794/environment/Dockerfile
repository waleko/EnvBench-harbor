FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/google/trax.git /data/project \
    && cd /data/project \
    && git checkout 14514794eb03247c3a4426032607e1f7547e6f63
