FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/jupyter/qtconsole.git /data/project \
    && cd /data/project \
    && git checkout 56e5a5ec5cfccf5afd098fe8bb5b2c558a1dc8f9
