FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/claritychallenge/clarity.git /data/project \
    && cd /data/project \
    && git checkout 5fa8741ed75eb9c9c8dba078c86b78458e2713f3
