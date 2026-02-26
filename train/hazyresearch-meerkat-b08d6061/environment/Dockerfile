FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/hazyresearch/meerkat.git /data/project \
    && cd /data/project \
    && git checkout b08d6061f7d3e0acdc04a6304cf8fc27c2d72b30
