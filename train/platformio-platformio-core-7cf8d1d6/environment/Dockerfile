FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/platformio/platformio-core.git /data/project \
    && cd /data/project \
    && git checkout 7cf8d1d6961761eab681d49eea7fbafae0889186
