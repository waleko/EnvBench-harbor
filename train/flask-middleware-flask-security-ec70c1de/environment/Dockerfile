FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/flask-middleware/flask-security.git /data/project \
    && cd /data/project \
    && git checkout ec70c1deac0530edfa8c4f4d1b545d0b5613af59
