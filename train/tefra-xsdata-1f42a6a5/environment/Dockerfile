FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/tefra/xsdata.git /data/project \
    && cd /data/project \
    && git checkout 1f42a6a5990664494049d4f97810cb0bcccc76df
