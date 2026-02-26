FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/eggpi/citationhunt.git /data/project \
    && cd /data/project \
    && git checkout 53d3975373b51c22a805cb2a07d12e3d8cfb21c7
