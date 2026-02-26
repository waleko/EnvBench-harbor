FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/meltano/sdk.git /data/project \
    && cd /data/project \
    && git checkout e4881b182b96f4f8c14bff059320dcf04715f65c
