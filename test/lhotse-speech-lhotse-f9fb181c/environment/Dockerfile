FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/lhotse-speech/lhotse.git /data/project \
    && cd /data/project \
    && git checkout f9fb181cbb733a95ebc2eda130d4db5b5a802677
