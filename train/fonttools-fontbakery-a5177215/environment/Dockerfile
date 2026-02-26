FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/fonttools/fontbakery.git /data/project \
    && cd /data/project \
    && git checkout a5177215f7c8e168416771637af17ae8935f273f
