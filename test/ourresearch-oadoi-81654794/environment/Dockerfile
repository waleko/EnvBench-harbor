FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ourresearch/oadoi.git /data/project \
    && cd /data/project \
    && git checkout 81654794d07009039221b4f96834dd254cefaec0
