FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/alteryx/featuretools.git /data/project \
    && cd /data/project \
    && git checkout 8c99ff7d62d723e90d406ac56bae22aad82e6a47
