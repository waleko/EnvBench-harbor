FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ajenti/ajenti.git /data/project \
    && cd /data/project \
    && git checkout af7a178ae8dc847a20c47e2cb0176bffecfea14c
