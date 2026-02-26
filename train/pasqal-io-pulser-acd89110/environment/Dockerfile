FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pasqal-io/pulser.git /data/project \
    && cd /data/project \
    && git checkout acd8911024ab3b1fced0ff746fbe2f38452b0da0
