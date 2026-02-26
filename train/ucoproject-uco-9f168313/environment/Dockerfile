FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ucoproject/uco.git /data/project \
    && cd /data/project \
    && git checkout 9f168313453bb577141248e3968198bc00e7d39b
