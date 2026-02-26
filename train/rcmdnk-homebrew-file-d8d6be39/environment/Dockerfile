FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/rcmdnk/homebrew-file.git /data/project \
    && cd /data/project \
    && git checkout d8d6be39755166e696dbbc4f16eb2e20dd2ee97c
