FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mause/duckdb_engine.git /data/project \
    && cd /data/project \
    && git checkout f196b338b383d597ebdb6bef69879e75e6a3edbb
