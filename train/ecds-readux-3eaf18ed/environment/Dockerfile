FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ecds/readux.git /data/project \
    && cd /data/project \
    && git checkout 3eaf18edb9bcb0858507dcdb9295bc367e1ff8fb
