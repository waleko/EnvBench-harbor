FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/python/importlib_metadata.git /data/project \
    && cd /data/project \
    && git checkout f3901686abc47853523f3b211873fc2b9e0c5ab5
