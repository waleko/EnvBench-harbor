FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pretalx/pretalx.git /data/project \
    && cd /data/project \
    && git checkout 64e72619ce413bbcbbe5b838d0bc8cf690d1c3a8
