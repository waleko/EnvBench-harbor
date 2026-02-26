FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/theislab/cellrank.git /data/project \
    && cd /data/project \
    && git checkout 6074913214f087301dd49bd9ef581c20ec56e759
