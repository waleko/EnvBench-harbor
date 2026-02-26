FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ibm/ibmi-bob.git /data/project \
    && cd /data/project \
    && git checkout d741050ea70c32474d58a5f0897ab0056d9a611e
