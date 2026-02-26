FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/bmun/huxley.git /data/project \
    && cd /data/project \
    && git checkout 271aeac9ebf5f83ae50763ba1463689e19d2d61a
