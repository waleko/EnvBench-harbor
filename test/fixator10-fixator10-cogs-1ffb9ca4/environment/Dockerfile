FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/fixator10/fixator10-cogs.git /data/project \
    && cd /data/project \
    && git checkout 1ffb9ca442879c6c025d209b20523dc3825070a5
