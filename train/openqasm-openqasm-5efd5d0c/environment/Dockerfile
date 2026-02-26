FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/openqasm/openqasm.git /data/project \
    && cd /data/project \
    && git checkout 5efd5d0c7fc506b3f1c33e44f0f401aadfd013e0
