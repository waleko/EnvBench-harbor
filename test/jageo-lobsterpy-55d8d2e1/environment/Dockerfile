FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/jageo/lobsterpy.git /data/project \
    && cd /data/project \
    && git checkout 55d8d2e119aa1147166994d57fbdbe10931cc748
