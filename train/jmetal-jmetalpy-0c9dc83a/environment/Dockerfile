FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/jmetal/jmetalpy.git /data/project \
    && cd /data/project \
    && git checkout 0c9dc83ab4534d2cf053a1d159613cdc58b42c57
