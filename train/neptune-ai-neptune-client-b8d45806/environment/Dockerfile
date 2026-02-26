FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/neptune-ai/neptune-client.git /data/project \
    && cd /data/project \
    && git checkout b8d45806f7d0a96beb45ab09d7ddec693253a9e7
