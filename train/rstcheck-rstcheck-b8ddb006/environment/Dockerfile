FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/rstcheck/rstcheck.git /data/project \
    && cd /data/project \
    && git checkout b8ddb006f1f49a9bdaf40e45f0bc0b070f460513
