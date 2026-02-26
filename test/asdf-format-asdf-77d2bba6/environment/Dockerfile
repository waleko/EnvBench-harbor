FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/asdf-format/asdf.git /data/project \
    && cd /data/project \
    && git checkout 77d2bba699ac3424e63c316f5aa29918e32f3268
