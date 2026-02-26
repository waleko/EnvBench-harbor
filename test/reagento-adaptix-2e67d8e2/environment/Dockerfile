FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/reagento/adaptix.git /data/project \
    && cd /data/project \
    && git checkout 2e67d8e2120388e2054414d8a3a99f047dca2f13
