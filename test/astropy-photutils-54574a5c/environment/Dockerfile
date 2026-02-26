FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/astropy/photutils.git /data/project \
    && cd /data/project \
    && git checkout 54574a5c2eac37024b985d4b720f398c0d2b68ca
