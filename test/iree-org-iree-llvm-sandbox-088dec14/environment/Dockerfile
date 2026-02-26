FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/iree-org/iree-llvm-sandbox.git /data/project \
    && cd /data/project \
    && git checkout 088dec146f1be4b2786766ff292781c6f9cdc736
