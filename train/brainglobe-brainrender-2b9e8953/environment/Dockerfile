FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/brainglobe/brainrender.git /data/project \
    && cd /data/project \
    && git checkout 2b9e89533cd7802802ef63c791245af7b33cc916
