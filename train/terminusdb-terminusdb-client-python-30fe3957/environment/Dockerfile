FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/terminusdb/terminusdb-client-python.git /data/project \
    && cd /data/project \
    && git checkout 30fe3957a2ccd4fe4c15b3d36fc5419bcf166a85
