FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/bdaiinstitute/spatialmath-python.git /data/project \
    && cd /data/project \
    && git checkout 43d9a95eb50b708a226f27b357c7c1baed3442ce
