FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/lest/prometheus-rpm.git /data/project \
    && cd /data/project \
    && git checkout c429f9bd2672903d66d4a67659efc2f5570884cb
