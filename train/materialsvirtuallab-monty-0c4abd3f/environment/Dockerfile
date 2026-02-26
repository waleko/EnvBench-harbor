FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/materialsvirtuallab/monty.git /data/project \
    && cd /data/project \
    && git checkout 0c4abd3f3256696be8aeaaf9e0c60d21faa2e476
