FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/intake/intake.git /data/project \
    && cd /data/project \
    && git checkout 7cc9d879f2f0de65552681f2055ed1e3367bc6da
