FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pyvisa/pyvisa.git /data/project \
    && cd /data/project \
    && git checkout df628ff00a0a4ae4efee5277738b12a9d2fd0da0
