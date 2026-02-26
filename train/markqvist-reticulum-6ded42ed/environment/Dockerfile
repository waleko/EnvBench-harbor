FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/markqvist/reticulum.git /data/project \
    && cd /data/project \
    && git checkout 6ded42edd7ae203e5a565cb70138c2d7b4b58b5b
