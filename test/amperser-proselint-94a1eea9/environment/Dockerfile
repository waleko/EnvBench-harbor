FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/amperser/proselint.git /data/project \
    && cd /data/project \
    && git checkout 94a1eea991ffc171a28115523876add890f78225
