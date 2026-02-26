FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/lichess4545/heltour.git /data/project \
    && cd /data/project \
    && git checkout 1d5fd89ae12e2e27cfa278c5cbaf0aa47325f030
