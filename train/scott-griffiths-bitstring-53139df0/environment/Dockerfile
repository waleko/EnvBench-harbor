FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/scott-griffiths/bitstring.git /data/project \
    && cd /data/project \
    && git checkout 53139df043335648546feb288a0ff7cbf6ddf876
