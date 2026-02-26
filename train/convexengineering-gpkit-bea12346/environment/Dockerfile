FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/convexengineering/gpkit.git /data/project \
    && cd /data/project \
    && git checkout bea1234606649dd11a2e59b610b2ba8b8c8adfae
