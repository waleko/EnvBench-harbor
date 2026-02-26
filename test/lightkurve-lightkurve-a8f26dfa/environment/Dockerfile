FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/lightkurve/lightkurve.git /data/project \
    && cd /data/project \
    && git checkout a8f26dfa8196e99d9bf93f71d51ad02cbcd826ea
