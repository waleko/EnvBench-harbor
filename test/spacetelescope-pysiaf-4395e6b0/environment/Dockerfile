FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/spacetelescope/pysiaf.git /data/project \
    && cd /data/project \
    && git checkout 4395e6b05a000853a26bc594854f299c73f198e7
