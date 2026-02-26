FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/yt-project/unyt.git /data/project \
    && cd /data/project \
    && git checkout c4220c71e80741a58ca83c561b2440b854bc69ef
