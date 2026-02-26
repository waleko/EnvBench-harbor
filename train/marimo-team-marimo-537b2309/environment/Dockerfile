FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/marimo-team/marimo.git /data/project \
    && cd /data/project \
    && git checkout 537b23093bb75afd57b2c1f1d2f5cd528a08fc66
