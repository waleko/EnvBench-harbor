FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/libensemble/libensemble.git /data/project \
    && cd /data/project \
    && git checkout 99934db94cac472649d4e452da20123d51e8cee1
