FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/rlberry-py/rlberry.git /data/project \
    && cd /data/project \
    && git checkout 81413717d8526a4890b5af05d1a27c747088b31d
