FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/calliope-project/calliope.git /data/project \
    && cd /data/project \
    && git checkout 4079fbd595d0e25504e977df0b22883507b2492e
