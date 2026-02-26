FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mov-cli/mov-cli.git /data/project \
    && cd /data/project \
    && git checkout 32f8af4f15804dd6ce88d8f781a12b918119e64c
