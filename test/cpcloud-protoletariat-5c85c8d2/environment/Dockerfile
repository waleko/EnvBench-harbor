FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/cpcloud/protoletariat.git /data/project \
    && cd /data/project \
    && git checkout 5c85c8d27fb6535108a1f2846f4f0bd820472541
