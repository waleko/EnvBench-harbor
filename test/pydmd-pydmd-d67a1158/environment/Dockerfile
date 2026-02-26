FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pydmd/pydmd.git /data/project \
    && cd /data/project \
    && git checkout d67a115805274b7862cb57d1ea4e4cd721412997
