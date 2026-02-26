FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/datamol-io/datamol.git /data/project \
    && cd /data/project \
    && git checkout 0312388b956e2b4eeb72d791167cfdb873c7beab
