FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/democracyclub/uk-polling-stations.git /data/project \
    && cd /data/project \
    && git checkout d67f5fc05c9aa40530b21dea0cc9d5db920f6493
