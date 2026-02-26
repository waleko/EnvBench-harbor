FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/starsimhub/starsim.git /data/project \
    && cd /data/project \
    && git checkout 0d3df5d3c57cfd89a8ccda8b3155c70a3b114e85
