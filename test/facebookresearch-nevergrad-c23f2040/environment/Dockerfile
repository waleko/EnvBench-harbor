FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/facebookresearch/nevergrad.git /data/project \
    && cd /data/project \
    && git checkout c23f20406d9223afbe253f9807ca7e8ba993a1ac
