FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/materialsproject/custodian.git /data/project \
    && cd /data/project \
    && git checkout bc9ecbb5c41fbc7a67b880af6cd804cba52ecd05
