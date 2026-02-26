FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/robotframework/robotframework.git /data/project \
    && cd /data/project \
    && git checkout dc42d589cf96edfffc0d7a6ce597c06916ddbc76
