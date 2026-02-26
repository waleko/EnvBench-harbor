FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pylabrobot/pylabrobot.git /data/project \
    && cd /data/project \
    && git checkout e899965b61d20a5343d44c162eb4095623f5f0ce
