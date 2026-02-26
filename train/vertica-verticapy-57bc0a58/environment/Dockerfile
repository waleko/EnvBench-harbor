FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/vertica/verticapy.git /data/project \
    && cd /data/project \
    && git checkout 57bc0a58ca9736d0907d2e6043d206afb4b4f6eb
