FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/astropy/reproject.git /data/project \
    && cd /data/project \
    && git checkout 529fb3ad7c0d2ac79dd65f851228457a9691064c
