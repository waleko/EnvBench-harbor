FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/cltk/cltk.git /data/project \
    && cd /data/project \
    && git checkout 7014616ecffa64d170a8e486b904bac04398cdb7
