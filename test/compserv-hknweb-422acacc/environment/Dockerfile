FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/compserv/hknweb.git /data/project \
    && cd /data/project \
    && git checkout 422acacc4b1a9a56fd6b5da07491662a114a97a8
