FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/democracyclub/everyelection.git /data/project \
    && cd /data/project \
    && git checkout 74e6fabf58668d8b96713d05f877b6e4f0353166
