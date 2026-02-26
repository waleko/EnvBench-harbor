FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/wpi-lnl/lnldb.git /data/project \
    && cd /data/project \
    && git checkout 6384c05c867ef1e34f80c3c38f5fabdc3f35d28b
