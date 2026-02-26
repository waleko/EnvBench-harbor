FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mflowgen/mflowgen.git /data/project \
    && cd /data/project \
    && git checkout 354619ca1c2a0f47b5db5f348fa5a7a12bc868d3
