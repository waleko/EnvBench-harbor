FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pypa/distutils.git /data/project \
    && cd /data/project \
    && git checkout 0de29d3545dd3bf72c7e64bf8a8e53eac2ee50e0
