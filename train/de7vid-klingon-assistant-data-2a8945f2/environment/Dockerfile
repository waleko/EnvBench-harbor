FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/de7vid/klingon-assistant-data.git /data/project \
    && cd /data/project \
    && git checkout 2a8945f261748cde5e84363ac5145ac74b7c5e61
